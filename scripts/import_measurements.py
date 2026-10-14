#!/usr/bin/env python3
"""Place measurements and their explanation in the same model/memory/test folder."""
import argparse
import hashlib
import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_MODEL = 'nvidia/Qwen3.8-27B-NVFP4'
DATE = '2026-10-14'
GROUPS = {'after30':'comparacion-de-memoria-y-concurrencia', 'memory':'pruebas-con-30-por-ciento',
          'short':'primeras-pruebas-con-historiales-cortos', 'context-40':'primeras-pruebas-con-historiales-largos',
          'reuse':'pruebas-de-historial-reutilizado', 'additional':'comparaciones-adicionales'}

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def model_folder(model):
    return ROOT/'modelos'/re.sub(r'[^a-z0-9.-]+','-',model.lower())

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source', default=str(pathlib.Path.home()/'.cache/TestsGB10/campana-2026-10-14'))
    source=pathlib.Path(parser.parse_args().source)
    used=set(); inventory=[]
    old_inventory=[]
    index=model_folder(DEFAULT_MODEL)/'configuracion-del-equipo'/DATE/'inventario-de-archivos-originales.json'
    if index.exists():old_inventory=json.loads(index.read_text())
    def copy(src,dst):
        dst.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(src,dst)
        used.add(src)
        inventory.append({'archivo':dst.relative_to(ROOT).as_posix(),
                          'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
    def metadata_for(path):
        for parent in path.parents:
            f=parent/'metadata.json'
            if f.exists():
                d=json.loads(f.read_text())
                if isinstance(d,dict):return d
            if parent==source:break
        return {}
    for path in sorted(source.rglob('*.json')):
        raw=json.loads(path.read_text())
        if not isinstance(raw,dict):continue
        s=raw.get('summary',{})
        legacy='model_id' in raw and 'mean_ttft_ms' in raw
        rejection='http_status' in raw and 'output_requested' in raw
        if not (legacy or rejection or 'input_tokens' in s):continue
        model=raw.get('model_id',s.get('model',DEFAULT_MODEL))
        mem=s.get('memory_fraction')
        mem=round(mem*100) if mem is not None else next((int(p.split('-')[1]) for p in path.parts if p.startswith('memory-')),40)
        seqs=s.get('server_max_num_seqs',4)
        context=s.get('max_model_len')
        meta=metadata_for(path)
        for profile in meta.get('profiles',[]):
            if round(profile['fraction']*100)==mem and profile.get('max_num_seqs',4)==seqs:
                context=context or profile.get('max_model_len')
        context=context or (131072 if mem==30 else 262144)
        initial=path.relative_to(source).parts[0] in ('short','context-40')
        control=path.relative_to(source).parts[0]=='additional' and mem==40 and seqs==4
        additional=path.relative_to(source).parts[0]=='additional'
        repeated=s.get('history_step') is not None or 'reuse' in path.parts or 'reuse-40' in path.parts
        phase=s.get('history_step') if s.get('history_step') is not None else int(path.stem[:2]) if repeated else None
        if legacy:
            count=raw['num_prompts'];concurrency=raw['max_concurrency']
            inp=raw['total_input_tokens']//count;out=raw['total_output_tokens']//count
        elif rejection:
            count=concurrency=1;inp=raw['input_tokens'];out=raw['output_requested']
        else:
            concurrency=s['concurrency'];count=s.get('num_requests',concurrency)
            inp=s['input_tokens'];out=s['output_tokens']
        suffix='-medicion-inicial' if initial else ''
        if control:suffix+='-repeticion-de-control'
        elif additional:suffix+='-comparacion-adicional'
        if s.get('request_timeout_s',1200)>1200:suffix+='-espera-ampliada'
        if repeated:
            suffix='-'+str(phase)+'-'+('historial-nuevo' if phase==1 else 'historial-repetido' if phase%2==0 else 'historial-ampliado')
        name=(f'{DATE}-{count}-conversaciones-hasta-{concurrency}-a-la-vez-{inp}-entrada-{out}-respuesta-servidor-{seqs}'+suffix)
        if rejection:name=DATE+'-rechazo-por-superar-el-limite-de-contexto'
        dest=model_folder(model)/f'memoria-{mem}-por-ciento'/name
        config={'tipo':'rechazo' if rejection else 'conversaciones', 'modelo':model,'fecha':DATE,
                'memoria_porcentaje':mem,'limite_servidor':seqs,'limite_contexto_configurado':context,
                'conversaciones_totales':count,'concurrencia_enviada':concurrency,
                'tokens_entrada':inp,'tokens_respuesta_pedidos':out,'medicion_inicial':initial,
                'repeticion_de_control':control,
                'comprobacion_adicional':additional,
                'espera_ampliada':s.get('request_timeout_s',1200)>1200,
                'historial_reutilizado':repeated,'paso_historial':phase}
        write(dest/'configuracion.json',config)
        copy(path,dest/'mediciones.json')
        if path.with_suffix('.log').exists():copy(path.with_suffix('.log'),dest/'registro-de-ejecucion.log')
    # Startup attempts are full test folders, including unsuccessful attempts.
    for path in sorted(source.rglob('metadata.json')):
        meta=json.loads(path.read_text())
        for profile in meta.get('profiles',[]):
            mem=round(profile['fraction']*100);seqs=profile.get('max_num_seqs',4)
            label='memory-'+str(mem)+(('-seqs-'+str(seqs)) if seqs!=4 else '')
            if profile.get('request_timeout_s',1200)>1200:
                label+='-timeout-'+str(profile['request_timeout_s'])
            for attempt in profile.get('attempts',[]):
                context=attempt['max_model_len'];model=meta.get('model',DEFAULT_MODEL)
                control=path.relative_to(source).parts[0]=='additional' and mem==40 and seqs==4
                additional=path.relative_to(source).parts[0]=='additional'
                suffix='-repeticion-de-control' if control else '-comparacion-adicional' if additional else ''
                if profile.get('request_timeout_s',1200)>1200:suffix+='-espera-ampliada'
                dest=model_folder(model)/f'memoria-{mem}-por-ciento'/f'{DATE}-arranque-contexto-{context}-servidor-{seqs}{suffix}'
                write(dest/'configuracion.json',{'tipo':'arranque','modelo':model,'fecha':DATE,
                    'memoria_porcentaje':mem,'limite_servidor':seqs,'limite_contexto_configurado':context,
                    'repeticion_de_control':control,'comprobacion_adicional':additional,
                    'espera_ampliada':profile.get('request_timeout_s',1200)>1200})
                write(dest/'mediciones.json',attempt)
                log=path.parent/label/f'startup-{context}.log'
                if log.exists():copy(log,dest/'registro-del-servidor.log')
    # Preserve every remaining original file, using descriptive archive names.
    technical=model_folder(DEFAULT_MODEL)/'configuracion-del-equipo'/DATE
    for path in sorted(source.rglob('*')):
        if not path.is_file() or path in used or path.suffix=='.tmp':continue
        rel=path.relative_to(source)
        group=GROUPS.get(rel.parts[0], 'plan-de-las-pruebas')
        parts=list(rel.parts[1:]) if len(rel.parts)>1 else [rel.name]
        renames={'metadata.json':'configuracion-y-estado.json','override.json':'ultimo-cambio-temporal.json',
                 'restored-server.log':'registro-de-restauracion.log','session.json':'plan-y-estado-general.json',
                 'server.log':'registro-del-servidor.log','summary.json':'resumen-original.json',
                 'planned-profiles.json':'configuraciones-previstas.json',
                 'runner-used.py':'script-de-bateria-ejecutado.py','probe-used.py':'script-de-medicion-ejecutado.py'}
        parts=[renames.get(part,part.replace('memory-','memoria-').replace('-seqs-','-limite-servidor-').replace('-timeout-','-espera-')) for part in parts]
        copy(path,technical/group/pathlib.Path(*parts))
    write(model_folder(DEFAULT_MODEL)/'configuracion-del-equipo'/'equipo.json',{
        'modelo':DEFAULT_MODEL,'contexto_maximo_del_modelo':262144,'memoria_total_gib':121.63,
        'pesos_del_modelo_gib':19.95,'imagen':'nvcr.io/nvidia/vllm:26.09-py3',
        'version_vllm':'0.29.0+5013de39.dev','revision_modelo':'482ca0f3832238542f8f5295dde86b5f22711d80',
        'configuracion_a_restaurar':{'memoria_porcentaje':40,'limite_servidor':4,'contexto_maximo':262144}})
    # A running test can produce its log before its first JSON snapshot. Once
    # both exist, keep that log beside the test and remove its earlier archive
    # copy only if it is still exactly the file we previously generated.
    current_paths={entry['archivo'] for entry in inventory}
    for entry in old_inventory:
        obsolete=ROOT/entry['archivo']
        if entry['archivo'] not in current_paths and obsolete.is_file() and obsolete.is_relative_to(ROOT/'modelos'):
            if hashlib.sha256(obsolete.read_bytes()).hexdigest()==entry['sha256']:
                obsolete.unlink()
    write(technical/'inventario-de-archivos-originales.json',inventory)
    print(f'Imported {len(inventory)} original files; explanations and data share each test folder.')

if __name__=='__main__':main()
