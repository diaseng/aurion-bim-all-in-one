from fastapi import APIRouter, UploadFile, File
import pandas as pd, tempfile, pdfplumber
router=APIRouter()
@router.get('/status')
def status(): return {'module':'saturno','ok':True}
@router.post('/sinapi/import')
def sinapi_import(file: UploadFile = File(...)):
    name = file.filename.lower()
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.'+name.split('.')[-1])
    tmp.write(file.file.read()); tmp.flush()
    if name.endswith('.xlsx'):
        df = pd.read_excel(tmp.name); sample = df.head(10).fillna('').to_dict(orient='records')
        return {'filename': name, 'type':'xlsx', 'rows': len(df), 'sample': sample}
    elif name.endswith('.csv'):
        df = pd.read_csv(tmp.name); sample = df.head(10).fillna('').to_dict(orient='records')
        return {'filename': name, 'type':'csv', 'rows': len(df), 'sample': sample}
    elif name.endswith('.pdf'):
        with pdfplumber.open(tmp.name) as pdf:
            text = ''.join([(p.extract_text() or '') for p in pdf.pages[:2]])
        return {'filename': name, 'type':'pdf', 'preview': text[:1200]}
    return {'filename': name, 'type':'unknown'}
@router.post('/quote')
def quote(discipline: str, quantity: float): return {'discipline': discipline, 'quantity': quantity, 'unit_cost': 100.0, 'total': 100.0*quantity}
