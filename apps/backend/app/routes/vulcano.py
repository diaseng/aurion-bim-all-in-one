from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'vulcano','ok':True}
@router.post('/lsf/frame')
def lsf_frame(span: float, height: float, spacing: float=0.6): return {'system':'LSF','members': int(span/spacing)+1}
@router.post('/concrete/generate')
def concrete_generate(beams:int=4, columns:int=6, fck: float=25.0): return {'system':'concrete_rc','beams':beams,'columns':columns,'fck_MPa':fck}
@router.post('/concrete/rebar')
def concrete_rebar(beam_len: float, beam_h: float, cover: float=0.03): return {'rebar_estimate_kg': round(beam_len*beam_h*7850*0.0005,2), 'cover':cover}
