from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .services.InvoicePdfServiceWeasy import InvoicePdfServiceWeasy
from django.http import HttpResponse

@api_view(['POST'])
def generateInvoice(request):
    """
    Generate invoice PDF from JSON data
    """
    try:
        invoice_data = request.data
        if not invoice_data:
            return Response(
                {'error': 'Invoice data is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        locale = request.query_params.get('locale', 'en')
            
        if locale not in ['en', 'bn']:
            locale = 'en'
        
        pdf_service = InvoicePdfServiceWeasy(locale)
        pdf_bytes = pdf_service.generate_invoice_pdf(invoice_data)
        
        # Return PDF
        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="invoice_{invoice_data.get("invoiceNumber", "document")}.pdf"'
        
        return response
        
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )