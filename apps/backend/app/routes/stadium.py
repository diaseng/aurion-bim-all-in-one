from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'stadium','ok':True}
@router.post('/generate')
def generate(kind:str='quadra_futsal', length:float=40, width:float=20): return {'kind':kind,'area_m2':length*width}
