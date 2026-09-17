import datetime as dt,json,os,pathlib,urllib.request
OUT=pathlib.Path('data');OUT.mkdir(exist_ok=True);token=os.getenv('BRAPI_TOKEN','')
headers={'User-Agent':'radar-b3-clean/2.0'}
if token:headers['Authorization']=f'Bearer {token}'
req=urllib.request.Request('https://brapi.dev/api/v2/tickers?type=stock&subType=stock&sortBy=symbol&sortOrder=asc&page=1&limit=2000',headers=headers)
with urllib.request.urlopen(req,timeout=90) as r:data=json.load(r)
items=[];seen=set();now=dt.datetime.now(dt.timezone.utc).isoformat()
for x in data.get('results',[]):
 t=(x.get('symbol') or '').upper()
 if not t or t.endswith('F') or t in seen or not any(c.isdigit() for c in t) or not x.get('isActive',True):continue
 seen.add(t);q=x.get('quote') or {}
 items.append({'ticker':t,'name':x.get('name') or x.get('longName') or t,'sector':x.get('sector'),'price':q.get('lastPrice'),'change':q.get('changePercent'),'volume':q.get('volume'),'marketCap':q.get('marketCap'),'source':'brapi','source_url':'https://brapi.dev/docs','updated_at':now})
(OUT/'catalog.json').write_text(json.dumps({'updated_at':now,'count':len(items),'items':items,'source':'brapi catalog rebuilt from zero'},ensure_ascii=False,allow_nan=False),encoding='utf-8')
(OUT/'ranking.json').write_text(json.dumps({'updated_at':now,'universe_size':0,'items':[],'message':'Ranking só será preenchido com dados publicados e validados.','source_policy':'Nenhum indicador é herdado da base antiga.'},ensure_ascii=False,allow_nan=False),encoding='utf-8')
print('CLEAN DATA',len(items))
