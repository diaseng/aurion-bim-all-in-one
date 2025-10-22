from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'netuno','ok':True}
@router.post('/network/water')
def water(fixture_count:int, pressure: float=20.0): return {'fixtures':fixture_count,'pressure':pressure}
