from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'janus','ok':True}
@router.get('/i18n')
def i18n(): return {'locales':['pt-BR','en','es'], 'default':'pt-BR'}
