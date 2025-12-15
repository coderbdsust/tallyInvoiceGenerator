from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.conf import settings
from django.template.loader import render_to_string
import os
from num2words_bd_inr import amount_in_words


class InvoicePdfServiceWeasy:
    
    def __init__(self, locale='en'):
        self.locale = locale
        self.font_dir = settings.FONT_DIR
    
    def generate_invoice_pdf(self, invoice_data):
        """Generate invoice PDF using WeasyPrint (better Bengali support)"""
        
        # Render HTML template
        html_content = self._generate_html(invoice_data)
        
        # CSS with font-face declarations
        css_content = self._generate_css()
        
        # Font configuration for better Bengali rendering
        font_config = FontConfiguration()
        
        # Generate PDF with font configuration
        pdf = HTML(string=html_content).write_pdf(
            stylesheets=[CSS(string=css_content, font_config=font_config)],
            font_config=font_config
        )
        
        return pdf
    
    
    def _generate_css(self):
        """Generate CSS with proper font declarations"""
        
        if self.locale == 'bn':
            font_family = 'NotoSansBengali'
            bold_font = os.path.join(self.font_dir, 'Noto_Sans_Bengali/static/NotoSansBengali-Bold.ttf')
            regular_font = os.path.join(self.font_dir, 'Noto_Sans_Bengali/static/NotoSansBengali-Regular.ttf')
            black_font = os.path.join(self.font_dir, 'Noto_Sans_Bengali/static/NotoSansBengali-Black.ttf')
            extrabold_font = os.path.join(self.font_dir, 'Noto_Sans_Bengali/static/NotoSansBengali-ExtraBold.ttf')
            light_font = os.path.join(self.font_dir, 'Noto_Sans_Bengali/static/NotoSansBengali-Light.ttf')
            medium_font = os.path.join(self.font_dir, 'Noto_Sans_Bengali/static/NotoSansBengali-Medium.ttf')
            semibold_font = os.path.join(self.font_dir, 'Noto_Sans_Bengali/static/NotoSansBengali-SemiBold.ttf')
        else:
            font_family = 'Poppins'
            bold_font = os.path.join(self.font_dir, 'Poppins/Poppins-Bold.ttf')
            regular_font = os.path.join(self.font_dir, 'Poppins/Poppins-Regular.ttf')
        
        css = f"""
        @font-face {{
            font-family: '{font_family}';
            src: url('file://{regular_font}') format('truetype');
            font-weight: 400;
            font-style: normal;
        }}
        
        @font-face {{
            font-family: '{font_family}';
            src: url('file://{bold_font}') format('truetype');
            font-weight: 700;
            font-style: normal;
        }}
        """
        
        # Add additional Bengali font weights if locale is Bengali
        if self.locale == 'bn':
            css += f"""
        @font-face {{
            font-family: '{font_family}';
            src: url('file://{light_font}') format('truetype');
            font-weight: 300;
            font-style: normal;
        }}
        
        @font-face {{
            font-family: '{font_family}';
            src: url('file://{medium_font}') format('truetype');
            font-weight: 500;
            font-style: normal;
        }}
        
        @font-face {{
            font-family: '{font_family}';
            src: url('file://{semibold_font}') format('truetype');
            font-weight: 600;
            font-style: normal;
        }}
        
        @font-face {{
            font-family: '{font_family}';
            src: url('file://{extrabold_font}') format('truetype');
            font-weight: 800;
            font-style: normal;
        }}
        
        @font-face {{
            font-family: '{font_family}';
            src: url('file://{black_font}') format('truetype');
            font-weight: 900;
            font-style: normal;
        }}
        """
        
        css += f"""
        @page {{
            margin: 5px;
        }}
        
        * {{
            font-family: '{font_family}', sans-serif;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            font-size: {"10pt" if self.locale == 'bn' else "9pt"};
            line-height: {"1.6" if self.locale == 'bn' else "1.4"};
            color: #333333;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-rendering: optimizeLegibility;
        }}
        """
        
        # Bengali-specific CSS
        if self.locale == 'bn':
            css += """
        body {
            font-feature-settings: 'liga' 1, 'calt' 1, 'clig' 1;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        
        td, th, p, div, span {
            word-break: normal;
            hyphens: none;
            white-space: normal;
        }
        """
        
        css += f"""
        .container {{
            padding: 0;
            margin: 25px;
        }}
        
        .header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            gap: 30px;
        }}
        
        .left-header {{
            flex: 1;
        }}
        
        .right-header {{
            flex: 1;
            text-align: right;
        }}
        
        .logo {{
            max-width: 120px;
            max-height: 50px;
            margin-bottom: 15px;
        }}
        
        .barcode {{
            max-width: 220px;
            max-height: 50px;
            margin-bottom: 15px;
            display: inline-block;
        }}
        
        .invoice-info, .company-info {{
            font-size: {"10pt" if self.locale == 'bn' else "9pt"};
        }}
        
        .invoice-info table, .company-info table {{
            width: 100%;
            border-collapse: collapse;
        }}
        
        .invoice-info td, .company-info td {{
            padding: {"3px 2px" if self.locale == 'bn' else "2px"};
            line-height: {"1.5" if self.locale == 'bn' else "1.4"};
        }}
        
        .text-right {{
            text-align: right;
        }}
        
        .text-left {{
            text-align: left;
        }}
        
        .text-center {{
            text-align: center;
        }}
        
        .bold {{
            font-weight: bold;
        }}
        
        .divider {{
            border-top: 1px dashed #808080;
            margin: 8px 0;
        }}
        
        .section-title {{
            font-weight: bold;
            font-size: {"11pt" if self.locale == 'bn' else "10pt"};
            margin-bottom: 5px;
        }}
        
        .product-table, .payment-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0;
        }}
        
        .product-table th, .payment-table th {{
            background-color: rgba(128, 128, 128, 0.1);
            padding: {"5px 4px" if self.locale == 'bn' else "4px"};
            font-weight: bold;
            border-top: 0.5px solid #808080;
            border-bottom: 0.5px solid #808080;
            text-align: center;
            line-height: {"1.5" if self.locale == 'bn' else "1.4"};
        }}
        
        .product-table td, .payment-table td {{
            padding: {"5px 4px" if self.locale == 'bn' else "4px"};
            border-bottom: 0.5px solid #808080;
            line-height: {"1.5" if self.locale == 'bn' else "1.4"};
        }}
        
        .summary-table {{
            margin-left: auto;
            width: 200px;
        }}
        
        .summary-table td {{
            padding: {"3px 2px" if self.locale == 'bn' else "2px"};
            line-height: {"1.5" if self.locale == 'bn' else "1.4"};
        }}
        
        .bottom-section {{
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
        }}
        
        .payment-section {{
            flex: 2;
            padding-right: 20px;
        }}
        
        .summary-section {{
            flex: 1;
        }}
        """
        
        return css
    
    def _generate_html(self, invoice_data):
        """Generate HTML content for the invoice"""
        
        # Format dates
        def format_date(date_array):
            if isinstance(date_array, list) and len(date_array) == 3:
                return f"{date_array[0]}-{date_array[1]:02d}-{date_array[2]:02d}"
            return str(date_array)
        
        invoice_date = format_date(invoice_data.get('invoiceDate', []))
        delivery_date = format_date(invoice_data.get('deliveryDate', []))
        
        org = invoice_data.get('ownerOrganization', {})
        customer = invoice_data.get('customer', {})
        
        html = f"""
        <!DOCTYPE html>
        <html lang="{"bn" if self.locale == 'bn' else "en"}" dir="ltr">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Invoice</title>
        </head>
        <body>
            <div class="container">
                <!-- Header Section -->
                <div class="header">
                    <div class="left-header">
                        {"<img src='" + invoice_data.get('ownerOrganization', {}).get('logoB64', '') + "' class='logo' />" if invoice_data.get('ownerOrganization', {}).get('logoB64') else ''}
                        
                        <div class="invoice-info">
                            <table>
                                <tr>
                                    <td class="bold text-left">Invoice No:</td>
                                    <td class="text-right">{invoice_data.get('invoiceNumber', '')}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">Invoice Date:</td>
                                    <td class="text-right">{invoice_date}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">Payment Status:</td>
                                    <td class="text-right">{invoice_data.get('invoiceStatus', '').replace('_', ' ').title()}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">Delivery Date:</td>
                                    <td class="text-right">{delivery_date}</td>
                                </tr>
                                <tr>
                                    <td class="bold text-left">Invoice Amount:</td>
                                    <td class="text-right bold">{invoice_data.get('totalAmount', 0):.2f}</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                    
                    <div class="right-header">
                        {"<img src='" + invoice_data.get('barcode', '') + "' class='barcode' />" if invoice_data.get('barcode') else ''}
                        
                        <div class="company-info">
                            <table>
                                <tr>
                                    <td class="text-left">Company Name:</td>
                                    <td class="text-right">{org.get('orgName', '')}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">Address:</td>
                                    <td class="text-right">{org.get('orgAddressLine', '')}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">Postcode:</td>
                                    <td class="text-right">{org.get('orgAddressPostcode', '')}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">TIN No:</td>
                                    <td class="text-right">{org.get('orgTinNumber', '')}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">VAT Number:</td>
                                    <td class="text-right">{org.get('orgVatNumber', '')}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">Email Address:</td>
                                    <td class="text-right">{org.get('orgEmail', '')}</td>
                                </tr>
                                <tr>
                                    <td class="text-left">Contact No:</td>
                                    <td class="text-right">{org.get('orgMobileNo', '')}</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
                
                <div class="divider"></div>
                
                <!-- Billing Address -->
                <div class="section-title">Billing Address</div>
                <table style="width: 100%;">
                    <tr>
                        <td style="width: 20%;">Customer Name:</td>
                        <td>{customer.get('name', '')}</td>
                    </tr>
                    <tr>
                        <td>Address:</td>
                        <td>{customer.get('address', '')}</td>
                    </tr>
                    <tr>
                        <td>Postcode:</td>
                        <td>{customer.get('postcode', '')}</td>
                    </tr>
                    <tr>
                        <td>Phone:</td>
                        <td>{customer.get('mobile', '')}</td>
                    </tr>
                    <tr>
                        <td>Email:</td>
                        <td>{customer.get('email', '')}</td>
                    </tr>
                </table>
                
                <div class="divider"></div>
                
                <!-- Purchase History -->
                <div class="section-title">Purchase History</div>
                <table class="product-table">
                    <thead>
                        <tr>
                            <th style="width: 5%;">SL</th>
                            <th style="width: 40%;">Product Details</th>
                            <th style="width: 20%;">Unit Rate</th>
                            <th style="width: 15%;">Units</th>
                            <th style="width: 20%;">Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        {self._generate_product_rows(invoice_data.get('productSales', []))}
                    </tbody>
                </table>
                
                <!-- Payment and Summary -->
                <div class="bottom-section">
                    <div class="payment-section">
                        <div class="section-title">Customer Payment History</div>
                        <table class="payment-table">
                            <thead>
                                <tr>
                                    <th>Date</th>
                                    <th>Method</th>
                                    <th>Ref#</th>
                                    <th>Amount</th>
                                </tr>
                            </thead>
                            <tbody>
                                {self._generate_payment_rows(invoice_data.get('payments', []))}
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="summary-section">
                        <table class="summary-table">
                            <tr>
                                <td>Sub Total:</td>
                                <td class="text-right">{invoice_data.get('productSubTotal', 0):.2f}</td>
                            </tr>
                            <tr>
                                <td>Total Tax: ({invoice_data.get('taxRate', 0)}%)</td>
                                <td class="text-right">{invoice_data.get('productTotalTax', 0):.2f}</td>
                            </tr>
                            <tr>
                                <td>Total Vat: ({invoice_data.get('vatRate', 0)}%)</td>
                                <td class="text-right">{invoice_data.get('productTotalVat', 0):.2f}</td>
                            </tr>
                            <tr>
                                <td>Total Discount:</td>
                                <td class="text-right">{invoice_data.get('totalDiscount', 0):.2f}</td>
                            </tr>
                            <tr>
                                <td>Delivery Charge:</td>
                                <td class="text-right">{invoice_data.get('deliveryCharge', 0):.2f}</td>
                            </tr>
                            <tr class="bold">
                                <td>Total Amount:</td>
                                <td class="text-right">{invoice_data.get('totalAmount', 0):.2f}</td>
                            </tr>
                            <tr>
                                <td>Total Paid:</td>
                                <td class="text-right">{invoice_data.get('totalPaid', 0):.2f}</td>
                            </tr>
                            <tr>
                                <td>Total Due:</td>
                                <td class="text-right">{invoice_data.get('remainingAmount', 0):.2f}</td>
                            </tr>
                        </table>
                    </div>
                </div>
                
                <div style="margin-top: 10px;">
                    <span class="bold">In words:</span> {self.convert_amount_to_words(invoice_data.get('totalAmount', 0))}
                </div>
                
                <div class="divider"></div>
                
                <!-- Notes -->
                <div class="section-title">Notes</div>
                <p>Thank you for your business! If you have any questions about this invoice, please contact us at contacts.tallyapp@gmail.com</p>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def _generate_product_rows(self, products):
        """Generate HTML rows for products"""
        rows = ""
        for idx, product in enumerate(products, 1):
            rows += f"""
            <tr>
                <td class="text-center">{idx}</td>
                <td>{product.get('name', '')} ({product.get('code', '')})</td>
                <td class="text-right">{product.get('pricePerUnit', 0):.2f}</td>
                <td class="text-center">{product.get('quantitySold', 0):.2f} ({product.get('unitType', '')})</td>
                <td class="text-right">{product.get('totalAmount', 0):.2f}</td>
            </tr>
            """
        return rows
    
    def _generate_payment_rows(self, payments):
        """Generate HTML rows for payments"""
        rows = ""
        for payment in payments:
            payment_date = payment.get('paymentDate', [])
            if isinstance(payment_date, list) and len(payment_date) == 3:
                date_str = f"{payment_date[0]}-{payment_date[1]:02d}-{payment_date[2]:02d}"
            else:
                date_str = str(payment_date)
            
            rows += f"""
            <tr>
                <td>{date_str}</td>
                <td>{payment.get('paymentMethod', '')}</td>
                <td>{payment.get('reference', '')}</td>
                <td class="text-right">{payment.get('amount', 0):.2f}</td>
            </tr>
            """
        return rows
    
    def convert_amount_to_words(self, amount):
        """Convert amount to words"""
        return amount_in_words(amount, 'BDT','en', rounding=True)