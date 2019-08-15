from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from io import BytesIO
from tthh.models import *




def index(request):
    print("Genero el PDF")
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "auncencias.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("GAD CANTON MORONA \nListado de Ausencias", styles['Heading1'])
    clientes.append(header)

    tipos = TipoAusencia.objects.all();

    headings = ("Empleado",tipos[0],tipos[1], tipos[2], tipos[3],tipos[4])
    allclientes = [(p.nombres+" "+p.apellidos,contarTipo(tipos[0].id,p.id)
    				,contarTipo(tipos[1].id,p.id),contarTipo(tipos[2].id,p.id)
    				,contarTipo(tipos[3].id,p.id),contarTipo(tipos[4].id,p.id)
    	) for p in Empleado.objects.all()]
    #print allclientes

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue),
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response


def contarTipo(id,id_empleado):
	len_tipo = Registro.objects.filter(tipo_ausencia=id,empleado=id_empleado)
	return str(len(len_tipo))
