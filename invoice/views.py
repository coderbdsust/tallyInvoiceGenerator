from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .services.InvoicePdfServiceWeasy import InvoicePdfServiceWeasy
from django.http import HttpResponse
import logging
from django.utils.translation import get_language_from_request

log = logging.getLogger(__name__)

@api_view(['POST'])
def generateInvoice(request):
    try:
        invoice_data = request.data
        
        if not invoice_data:
            log.warning("Invoice generation failed: No invoice data provided")
            return Response(
                {'error': 'Invoice data is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Django's built-in language detection
        locale = get_language_from_request(request, check_path=False)

        log.info(f"Request Method: {request.method}")
        log.info(f"Content-Type: {request.content_type}")
        log.info(f"Content-Length: {request.META.get('CONTENT_LENGTH', 'Unknown')}")
        log.info(f"Accept-Language Header: {request.META.get('HTTP_ACCEPT_LANGUAGE', 'None')}")
        log.info(f"Detected Locale: {locale}")
        
        # Map Django locale codes to your supported locales
        locale_map = {
            'bn': 'bn',
            'bn-bd': 'bn',
            'en': 'en',
            'en-us': 'en',
            'en-gb': 'en',
        }
        
        locale = locale_map.get(locale.lower(), 'en')
        log.info(f"Mapped Locale: {locale}")
        
        pdf_service = InvoicePdfServiceWeasy(locale)
        pdf_bytes = pdf_service.generate_invoice_pdf(invoice_data)
        
        log.info(f"Invoice PDF generated successfully for invoice number: {invoice_data.get('invoiceNumber', 'Unknown')}, Size: {len(pdf_bytes)} bytes")
        
        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="invoice_{invoice_data.get("invoiceNumber", "document")}.pdf"'
        
        return response
        
    except Exception as e:
        log.error(f"Error generating invoice: {str(e)}", exc_info=True)
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )