from fastapi import APIRouter
import csv, tempfile, ezdxf
router=APIRouter()
@router.get('/status')
def status(): return {'module':'vesta','ok':True}
@router.post('/elements/wall')
def wall(length: float, height: float, thickness: float): return {'ifc':'IFCWall','params':locals()}
@router.post('/decor/floor_pagination')
def floor_pagination(pattern: str='retangular', tile_w: float=0.6, tile_h: float=0.6): return {'pattern':pattern,'tile_size':[tile_w,tile_h]}
@router.post('/kitchen/cutlist/import')
def kitchen_cutlist(): return {'status':'ok','note':'import plano de corte (CSV/DXF) - placeholder'}
@router.post('/annotations/tags/csv')
def tags_csv():
    rows=[('Etiqueta','Valor'),('Ambiente','Sala'),('Largura','3.40m')]
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    with open(tmp.name,'w',newline='',encoding='utf-8') as f: csv.writer(f).writerows(rows)
    return {'status':'ok','csv_path': tmp.name}
@router.post('/annotations/dimensions/dxf')
def dims_dxf():
    doc=ezdxf.new(dxfversion='R2010'); msp=doc.modelspace()
    msp.add_line((0,0),(3,0)); msp.add_line((0,0),(0,2.8))
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.dxf'); doc.saveas(tmp.name)
    return {'status':'ok','dxf_path': tmp.name}
