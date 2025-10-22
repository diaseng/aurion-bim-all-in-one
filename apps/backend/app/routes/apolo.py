from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'apolo','ok':True}
@router.post('/pv/estimate')
def pv(area_m2: float, efficiency: float=0.18, irrad_kwh_m2_day: float=4.5):
    kwp = area_m2*efficiency*0.2
    gen = kwp*irrad_kwh_m2_day*30
    return {'kwp': round(kwp,3), 'kwh_month': round(gen,1)}
