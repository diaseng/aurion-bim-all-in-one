from fastapi import APIRouter, UploadFile, File, HTTPException
router=APIRouter()
@router.get('/status')
def status(): return {'module':'mercurio','ok':True}
@router.post('/import')
def ingest(file: UploadFile = File(...)): return {'filename': file.filename, 'format': file.filename.split('.')[-1].lower()}
@router.post('/scale/convert')
def scale_convert(value: float, from_unit: str='mm', to_unit: str='m', scale: str='1:50'):
    U={'mm':0.001,'cm':0.01,'m':1.0}
    try: a,b = map(float, scale.split(':'))
    except: raise HTTPException(400,'escala inválida')
    if from_unit not in U or to_unit not in U: raise HTTPException(400,'unidade inválida')
    return {'value': value*U[from_unit]*(a/b)/U[to_unit], 'unit': to_unit}
