import ast, copy, importlib.util, pathlib, random
p=pathlib.Path(__file__).with_name('capacity_probe_v2.py')
spec=importlib.util.spec_from_file_location('probe_v2',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
assert m.growth_message_target(133632,133690,262144)==133690
assert m.growth_message_target(133632,133600,262144)==133632
assert m.growth_output_budget(1024,132605,262144)==1024
assert m.growth_output_budget(1024,261120,262144)==768
assert m.growth_output_budget(1024,262016,262144,True)==128
try:m.growth_message_target(262016,262017,262144,True)
except ValueError:pass
else:raise AssertionError('Must not remove history when the full context is exhausted')
class Args:turns=257;growth_stop_context=None;model="test"
# Exercise the real nested sizing function with a deterministic tokenizer.
fn=next(n for n in ast.walk(ast.parse(p.read_text())) if isinstance(n,ast.FunctionDef) and n.name=='add_small_message')
ns={'a':Args(),'model_info':{'max_model_len':262144},'growth_message_target':m.growth_message_target,
    'tokenize':lambda messages:sum(len(v['content']) for v in messages),
    'post':lambda endpoint,payload:{'count':len(payload['prompt'])}}
exec(compile(ast.Module(body=[fn],type_ignores=[]),str(p),'exec'),ns)
for nominal in (1024,1800):
 messages=[{'role':'system','content':'s'*60},{'role':'user','content':'u'*60},{'role':'assistant','content':'a'*1003}]
 before=copy.deepcopy(messages)
 info=ns['add_small_message'](messages,'Resume las decisiones.',nominal,random.Random(1),130)
 assert messages[:-1]==before
 actual=ns['tokenize'](messages)
 assert info['effective_input_target']-32<=actual<=info['effective_input_target']
 assert info['effective_input_target']==max(nominal,info['minimum_input_with_new_message'])
print('PASS: long-reply regression, unchanged history, ordinary sizing, closing reserve, and context exhaustion')
