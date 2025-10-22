from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'minerva','ok':True,'codex_scope':'P&D only'}
@router.post('/massing/generate')
def massing(lat: float=-23.55, lon: float=-46.63, levels:int=5): return {'status':'ok','ifc':'central_placeholder.ifc','levels':levels,'georef':[lat,lon]}
@router.post('/assistant/typology')
def typology(kind:str='residencial_multifamiliar', finish:str='intermediario'): return {'suggestion':'layout inicial gerado','kind':kind,'finish':finish}
