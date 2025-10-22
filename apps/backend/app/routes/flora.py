from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'flora','ok':True}
@router.post('/decor/rocks')
def rocks(style:str='basalto', amount:int=50): return {'rocks':amount,'style':style}
