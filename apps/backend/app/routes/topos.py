from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'topos','ok':True}
@router.post('/cutfill')
def cutfill(cut: float, fill: float): return {'cut_m3':cut,'fill_m3':fill,'balance_m3':fill-cut}
@router.post('/implantation')
def implantation(slope_percent: float): return {'advice':'boas práticas','slope_percent':slope_percent}
