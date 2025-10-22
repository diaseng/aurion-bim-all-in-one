from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import health, mercurio, vesta, vulcano, netuno, jupiter, apolo, flora, naiade, saturno, topos, hermes, cef, stadium, diana, minerva, janus
app=FastAPI(title='AURION BIM API',version='4.0')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
for r,p,t in [(health.router,'/health',['health']),(mercurio.router,'/mercurio',['mercurio']),(vesta.router,'/vesta',['vesta']),(vulcano.router,'/vulcano',['vulcano']),(netuno.router,'/netuno',['netuno']),(jupiter.router,'/jupiter',['jupiter']),(apolo.router,'/apolo',['apolo']),(flora.router,'/flora',['flora']),(naiade.router,'/naiade',['naiade']),(saturno.router,'/saturno',['saturno']),(topos.router,'/topos',['topos']),(hermes.router,'/hermes',['hermes']),(cef.router,'/cef',['cef']),(stadium.router,'/stadium',['stadium']),(diana.router,'/diana',['diana']),(minerva.router,'/minerva',['minerva']),(janus.router,'/janus',['janus'])]: app.include_router(r, prefix=p, tags=t)
@app.get('/')
def root(): return {'name':'AURION BIM API','version':'4.0'}
