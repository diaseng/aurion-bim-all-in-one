from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'cef','ok':True}
@router.post('/planilha/preencher')
def planilha(tipo:str='MCMV'): return {'status':'ok','tipo':tipo,'note':'preenchimento automático template'}
