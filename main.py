from fasthtml.common import *
from monsterui.all import *

app, rt = fast_app(hdrs=Theme.slate.headers())

@rt
def index():
    """A simple page generated with Monster UI, resembling aspects of the pasted text examples."""

    # Updated Navigation Bar (styled like InvoiceAI using Tailwind classes)
    navbar = Div(cls="flex justify-between items-center w-full")(
        A("Invoice<span>AI</span>", href="#", cls="text-2xl font-bold text-indigo-500", raw=True),
        Div(cls="hidden md:block")(
            Ul(cls="flex space-x-8")(
                Li(A("Features", href="#features", cls="text-gray-600 font-medium hover:text-indigo-500 transition-colors")),
                Li(A("How It Works", href="#how-it-works", cls="text-gray-600 font-medium hover:text-indigo-500 transition-colors")),
                Li(A("Pricing", href="#pricing", cls="text-gray-600 font-medium hover:text-indigo-500 transition-colors")),
                Li(A("Testimonials", href="#testimonials", cls="text-gray-600 font-medium hover:text-indigo-500 transition-colors")),
                Li(A("FAQ", href="#faq", cls="text-gray-600 font-medium hover:text-indigo-500 transition-colors"))
            )
        ),
        Div(cls="flex items-center space-x-4")(
            A("Try For Free", href="#", cls="bg-indigo-500 hover:bg-indigo-600 text-white px-5 py-2 rounded-lg font-medium transition-colors"),
            Button("☰", cls="md:hidden bg-transparent border-0 text-2xl text-gray-700 cursor-pointer")
        )
    )
    
    # Wrap the navbar in a header with container
    header = Div(cls="sticky top-0 bg-white bg-opacity-95 backdrop-blur-sm z-50 shadow-sm py-4")(
        Div(cls="container mx-auto px-4")(navbar)
    )

    # Hero Section (styled like InvoiceAI using Tailwind classes)
    hero = Div(cls="py-24 bg-gradient-to-r from-indigo-50 to-purple-50 relative overflow-hidden")(
        Container(
            Div(cls="max-w-2xl relative z-10")(
                H1("Extract Key Information From Invoices Automatically", 
                   cls="text-4xl md:text-5xl font-bold text-gray-900 leading-tight mb-6"),
                P("Our AI-powered invoice parser extracts dates, amounts, vendor details, and line items with 99.5% accuracy, saving your team hours of manual data entry.", 
                  cls="text-xl text-gray-600 mb-8"),
                Div(cls="flex flex-wrap gap-4")(
                    A("Start Free Trial", href="#", 
                      cls="bg-indigo-500 hover:bg-indigo-600 text-white px-6 py-3 rounded-lg font-medium transition-colors"),
                    A("Watch Demo", href="#", 
                      cls="bg-white text-indigo-500 border border-indigo-500 px-6 py-3 rounded-lg font-medium hover:bg-gray-50 transition-colors")
                )
            ),
            Div(cls="absolute right-0 top-1/2 transform -translate-y-1/2 hidden md:block")(
                Img(src="/placeholder.svg?height=500&width=600", alt="Invoice Parser Dashboard", 
                    cls="w-full max-w-2xl")
            ),
            cls="relative"
        )
    )

    # Features Section (styled like InvoiceAI using Tailwind classes)
    features_data = [
        {
            "title": "Intelligent Data Extraction", 
            "description": "Our AI automatically identifies and extracts key fields like invoice numbers, dates, amounts, tax details, and line items.",
            "icon": "🔍"
        },
        {
            "title": "Multi-Format Support", 
            "description": "Process invoices in any format - PDF, images, scans, emails, or even handwritten documents with high accuracy.",
            "icon": "📊"
        },
        {
            "title": "Seamless Integration", 
            "description": "Connect with QuickBooks, Xero, SAP, NetSuite, and other accounting systems for automated data transfer.",
            "icon": "🔄"
        },
        {
            "title": "Mobile Capture", 
            "description": "Scan invoices on-the-go with our mobile app and process them instantly, perfect for field workers and remote teams.",
            "icon": "📱"
        },
        {
            "title": "Data Validation", 
            "description": "Automatic validation checks ensure extracted data is accurate, with flagging of potential errors for review.",
            "icon": "🔒"
        },
        {
            "title": "Spend Analytics", 
            "description": "Gain insights into your spending patterns with detailed reports and dashboards based on your invoice data.",
            "icon": "📈"
        }
    ]

    def FeatureCard(feature):
        return Div(cls="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow")(
            Div(cls="bg-indigo-100 w-14 h-14 rounded-xl flex items-center justify-center mb-5 text-2xl")(
                feature["icon"]
            ),
            H3(feature["title"], cls="text-xl font-semibold mb-3 text-gray-900"),
            P(feature["description"], cls="text-gray-600")
        )

    features_section = Div(cls="py-20 bg-gray-50")(
        Container(
            Div(cls="text-center mb-16")(
                H2("Powerful Invoice Processing Features", cls="text-3xl md:text-4xl font-bold text-gray-900 mb-4"),
                P("Extract, validate, and organize invoice data with precision and speed", 
                  cls="text-xl text-gray-600 max-w-3xl mx-auto")
            ),
            Div(cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8")(
                *[FeatureCard(f) for f in features_data]
            )
        )
    )
    
    # How It Works Section (using MonsterUI Steps component)
    def ProcessStep(number, title, description, is_active=False, is_completed=False):
        return LiStep(
            Div(
                H3(title, cls="text-xl font-semibold mb-3 text-gray-900"),
                P(description, cls="text-gray-600 max-w-xs mx-auto"),
                cls="text-center"
            ),
            data_content=str(number),
            cls=StepT.success if is_completed else StepT.primary if is_active else StepT.neutral
        )

    how_it_works = Div(cls="py-24 bg-gray-50")(
        Container(
            Div(cls="text-center mb-16")(
                H2("How Our Invoice Parser Works", 
                   cls="text-3xl md:text-4xl font-bold text-gray-900 mb-6 tracking-tight"),
                P("Three simple steps to automate your invoice processing", 
                  cls="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed")
            ),
            Steps(
                ProcessStep(
                    "1",
                    "Upload Invoices",
                    "Upload invoices via drag-and-drop, email forwarding, mobile scan, or API integration with your existing systems.",
                    is_active=True
                ),
                ProcessStep(
                    "2",
                    "AI Processing",
                    "Our AI engine analyzes the document, identifies key fields, and extracts data with high precision in seconds."
                ),
                ProcessStep(
                    "3",
                    "Review & Export",
                    "Verify extracted data in our user-friendly interface and export to your accounting software or download as CSV/Excel."
                ),
                cls="w-full max-w-5xl mx-auto"
            )
        )
    )

    # Pricing Section (styled like InvoiceAI using Tailwind classes)
    pricing_section = Div(cls="py-24 bg-white", id="pricing")(
        Container(
            Div(cls="text-center mb-16")(
                H2("Simple, Transparent Pricing", 
                   cls="text-3xl md:text-4xl font-bold text-gray-900 mb-4"),
                P("Choose the plan that works best for your business", 
                  cls="text-xl text-gray-600 max-w-3xl mx-auto")
            ),
            # Updated toggle using MonsterUI components
            Div(cls="flex justify-center items-center gap-4 mb-12")(
                DivFullySpaced(
                    Span("Monthly", cls="font-medium text-gray-900"),
                    Switch(id="billing-toggle", checked=False),
                    Div(
                        Span("Annually ", cls="font-medium text-gray-500"),
                        Span("(Save 20%)", cls="text-sm text-gray-500")
                    ),
                    cls="flex items-center justify-center gap-4 w-fit"
                )
            ),
            Div(cls="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto")(
                # Starter Plan
                Div(cls="bg-white p-8 rounded-lg border border-gray-200 shadow-sm hover:shadow-md transition-shadow")(
                    H3("Starter", cls="text-xl font-bold mb-4 text-gray-900"),
                    Div(cls="flex items-end mb-6")(
                        Span("$49", cls="text-4xl font-bold text-gray-900"),
                        Span("/month", cls="text-gray-500 ml-1")
                    ),
                    Ul(cls="space-y-3 mb-8")(
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Up to 100 invoices/month", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Basic data extraction", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Email support", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("CSV/Excel export", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("90% accuracy guarantee", cls="text-gray-800 text-base")
                        )
                    ),
                    A("Get Started", href="#", cls="block w-full py-3 px-4 bg-indigo-500 hover:bg-indigo-600 text-white text-center rounded-lg font-medium transition-colors")
                ),
                
                # Business Plan (Popular)
                Div(cls="bg-white p-8 rounded-lg border-2 border-indigo-500 shadow-md hover:shadow-lg transition-shadow relative transform md:scale-105")(
                    Div(cls="absolute top-0 right-0 bg-indigo-500 text-white py-1 px-4 text-sm font-medium rounded-bl-lg rounded-tr-lg")(
                        "Popular"
                    ),
                    H3("Business", cls="text-xl font-bold mb-4 text-gray-900"),
                    Div(cls="flex items-end mb-6")(
                        Span("$149", cls="text-4xl font-bold text-gray-900"),
                        Span("/month", cls="text-gray-500 ml-1")
                    ),
                    Ul(cls="space-y-3 mb-8")(
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Up to 500 invoices/month", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Advanced data extraction", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Line item extraction", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("QuickBooks & Xero integration", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Priority support", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("98% accuracy guarantee", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Custom field mapping", cls="text-gray-800 text-base")
                        )
                    ),
                    A("Get Started", href="#", cls="block w-full py-3 px-4 bg-indigo-500 hover:bg-indigo-600 text-white text-center rounded-lg font-medium transition-colors")
                ),
                
                # Enterprise Plan
                Div(cls="bg-white p-8 rounded-lg border border-gray-200 shadow-sm hover:shadow-md transition-shadow")(
                    H3("Enterprise", cls="text-xl font-bold mb-4 text-gray-900"),
                    Div(cls="flex items-end mb-6")(
                        Span("$399", cls="text-4xl font-bold text-gray-900"),
                        Span("/month", cls="text-gray-500 ml-1")
                    ),
                    Ul(cls="space-y-3 mb-8")(
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Unlimited invoices", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Full-suite data extraction", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("All integrations included", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Dedicated account manager", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Custom AI training", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("99.5% accuracy guarantee", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("API access", cls="text-gray-800 text-base")
                        ),
                        Li(cls="flex items-start")(
                            Span("✓", cls="text-green-500 font-bold mr-2"),
                            Span("Advanced analytics", cls="text-gray-800 text-base")
                        )
                    ),
                    A("Contact Sales", href="#", cls="block w-full py-3 px-4 bg-indigo-500 hover:bg-indigo-600 text-white text-center rounded-lg font-medium transition-colors")
                )
            )
        )
    )

    # Testimonials Section (styled like InvoiceAI using Tailwind classes)
    testimonials_section = Div(cls="py-24 bg-gray-50", id="testimonials")(
        Container(
            Div(cls="text-center mb-16")(
                H2("What Our Customers Say", 
                   cls="text-3xl md:text-4xl font-bold text-gray-900 mb-6 tracking-tight"),
                P("Trusted by thousands of businesses worldwide", 
                  cls="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed")
            ),
            Div(cls="grid grid-cols-1 md:grid-cols-3 gap-8")(
                # First Testimonial
                Card(
                    DivLAligned(
                        DiceBearAvatar("Robert Chen", h=24, w=24),
                        Div(
                            H3("Robert Chen"),
                            P("Accounts Payable Manager, TechSolutions")
                        )
                    ),
                    P(cls="text-gray-600 my-6 leading-relaxed")(
                        "The accuracy of the data extraction is impressive. Even with our complex supplier invoices from multiple countries, InvoiceAI consistently pulls the right information with minimal errors."
                    ),
                    footer=DivFullySpaced(
                        DivHStacked(UkIcon("map-pin", height=16), P("New York, USA")),
                        DivHStacked(*(UkIconLink(icon, height=16) for icon in ("mail", "linkedin")))
                    ),
                    cls=CardT.hover
                ),
                # Second Testimonial
                Card(
                    DivLAligned(
                        DiceBearAvatar("Jennifer Patel", h=24, w=24),
                        Div(
                            H3("Jennifer Patel"),
                            P("CFO, Global Logistics Inc.")
                        )
                    ),
                    P(cls="text-gray-600 my-6 leading-relaxed")(
                        "We've reduced our invoice processing time by 80% since implementing InvoiceAI. What used to take our team days now happens in minutes, and with fewer errors."
                    ),
                    footer=DivFullySpaced(
                        DivHStacked(UkIcon("map-pin", height=16), P("London, UK")),
                        DivHStacked(*(UkIconLink(icon, height=16) for icon in ("mail", "linkedin")))
                    ),
                    cls=CardT.hover
                ),
                # Third Testimonial
                Card(
                    DivLAligned(
                        DiceBearAvatar("Sarah Johnson", h=24, w=24),
                        Div(
                            H3("Sarah Johnson"),
                            P("Owner, Bright Designs Studio")
                        )
                    ),
                    P(cls="text-gray-600 my-6 leading-relaxed")(
                        "As a small business owner, I was drowning in paperwork. InvoiceAI has been a game-changer for us. The QuickBooks integration works flawlessly, and I've reclaimed hours of my week."
                    ),
                    footer=DivFullySpaced(
                        DivHStacked(UkIcon("map-pin", height=16), P("Berlin, Germany")),
                        DivHStacked(*(UkIconLink(icon, height=16) for icon in ("mail", "linkedin")))
                    ),
                    cls=CardT.hover
                )
            )
        )
    )
    
    # FAQ Section (styled like InvoiceAI using Tailwind classes)
    faq_items = [
        {
            "question": "What types of invoices can your system process?",
            "answer": "Our invoice parser can process virtually any invoice format including PDFs, scanned images (JPG, PNG, TIFF), emails, and even handwritten invoices. We support invoices from any vendor or country, in multiple languages, and can handle both digital and physical documents with high accuracy."
        },
        {
            "question": "How accurate is the data extraction?",
            "answer": "Our system achieves 98-99.5% accuracy depending on your plan. The Enterprise plan includes custom AI training on your specific invoice formats to achieve the highest possible accuracy. All extracted data undergoes validation checks, and any uncertain fields are flagged for human review."
        },
        {
            "question": "Which accounting systems do you integrate with?",
            "answer": "We offer direct integrations with popular accounting systems including QuickBooks (Online and Desktop), Xero, Sage, NetSuite, SAP, Microsoft Dynamics, and FreshBooks. We also provide API access and CSV/Excel exports for custom integrations with any other system."
        },
        {
            "question": "Is my invoice data secure?",
            "answer": "Absolutely. We take security very seriously. All data is encrypted both in transit and at rest using bank-level encryption. We are SOC 2 Type II compliant, GDPR compliant, and we never share your data with third parties. We also offer data retention controls to automatically delete processed invoices after a specified period."
        },
        {
            "question": "How long does it take to process an invoice?",
            "answer": "Most invoices are processed within 5-10 seconds. Complex invoices with many line items or poor image quality may take up to 30 seconds. Batch processing allows you to upload hundreds of invoices at once, which are then processed in parallel for maximum efficiency."
        }
    ]
    
    def FaqItem(item):
        return Div(cls="border-b border-gray-200 py-5")(
            Button(cls="flex justify-between items-center w-full text-left font-semibold text-gray-900 focus:outline-none")(
                Span(item["question"]),
                Span("+", cls="text-xl text-indigo-500")
            ),
            Div(cls="mt-3 text-gray-600 hidden")(
                P(item["answer"])
            )
        )
    
    faq_section = Div(cls="py-20 bg-white", id="faq")(
        Container(
            Div(cls="text-center mb-16")(
                H2("Frequently Asked Questions", cls="text-3xl md:text-4xl font-bold text-gray-900 mb-4"),
                P("Find answers to common questions about our invoice parser", 
                  cls="text-xl text-gray-600 max-w-3xl mx-auto")
            ),
            Div(cls="max-w-3xl mx-auto")(
                *[FaqItem(item) for item in faq_items]
            ),
            # Note: In a real implementation, you would add JavaScript to toggle the visibility of answers
            Script("""
                document.addEventListener('DOMContentLoaded', function() {
                    const faqButtons = document.querySelectorAll('#faq button');
                    faqButtons.forEach(button => {
                        button.addEventListener('click', function() {
                            const answer = this.nextElementSibling;
                            const plusSign = this.querySelector('span:last-child');
                            
                            if (answer.classList.contains('hidden')) {
                                answer.classList.remove('hidden');
                                plusSign.textContent = '−';
                            } else {
                                answer.classList.add('hidden');
                                plusSign.textContent = '+';
                            }
                        });
                    });
                });
            """)
        )
    )
    
    # CTA Section (styled like InvoiceAI using Tailwind classes)
    cta_section = Div(cls="py-20 bg-indigo-600 text-white")(
        Container(
            Div(cls="text-center max-w-3xl mx-auto")(
                H2("Ready to Automate Your Invoice Processing?", 
                   cls="text-3xl md:text-4xl font-bold mb-6"),
                P("Join thousands of businesses that save time and reduce errors with our intelligent invoice parser.", 
                  cls="text-xl mb-10"),
                Div(cls="flex flex-wrap justify-center gap-4")(
                    A("Start Free Trial", href="#", 
                      cls="bg-white text-indigo-600 hover:bg-gray-100 px-8 py-4 rounded-lg font-medium transition-colors"),
                    A("Schedule Demo", href="#", 
                      cls="bg-transparent border-2 border-white text-white hover:bg-indigo-700 px-8 py-4 rounded-lg font-medium transition-colors")
                )
            )
        )
    )

    # Footer (styled like InvoiceAI using Tailwind classes)
    footer = Div(cls="bg-gray-900 text-white py-16")(
        Container(
            Div(cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-10")(
                Div(
                    Div(cls="text-2xl font-bold mb-4")("Invoice<span>AI</span>", raw=True),
                    P(cls="text-gray-400 mb-6")("Intelligent invoice parsing solution that extracts key information automatically with high accuracy."),
                    Div(cls="flex space-x-4")(
                        A(href="#", cls="bg-gray-800 hover:bg-indigo-500 w-10 h-10 rounded-full flex items-center justify-center transition-colors")("T"),
                        A(href="#", cls="bg-gray-800 hover:bg-indigo-500 w-10 h-10 rounded-full flex items-center justify-center transition-colors")("F"),
                        A(href="#", cls="bg-gray-800 hover:bg-indigo-500 w-10 h-10 rounded-full flex items-center justify-center transition-colors")("L"),
                        A(href="#", cls="bg-gray-800 hover:bg-indigo-500 w-10 h-10 rounded-full flex items-center justify-center transition-colors")("I")
                    )
                ),
                Div(
                    H4(cls="text-lg font-semibold mb-5")("Product"),
                    Ul(cls="space-y-3")(
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Features")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Pricing")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Integrations")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("API")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Updates"))
                    )
                ),
                Div(
                    H4(cls="text-lg font-semibold mb-5")("Resources"),
                    Ul(cls="space-y-3")(
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Documentation")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Guides")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Blog")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Support Center")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Webinars"))
                    )
                ),
                Div(
                    H4(cls="text-lg font-semibold mb-5")("Company"),
                    Ul(cls="space-y-3")(
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("About Us")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Careers")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Contact Us")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Partners")),
                        Li(A(href="#", cls="text-gray-400 hover:text-white transition-colors")("Legal"))
                    )
                )
            ),
            Div(cls="pt-8 border-t border-gray-800 flex flex-col md:flex-row justify-between items-center")(
                P(cls="text-gray-500 mb-4 md:mb-0")("© 2025 InvoiceAI. All rights reserved."),
                Div(cls="flex space-x-6")(
                    A(href="#", cls="text-gray-500 hover:text-white transition-colors")("Privacy Policy"),
                    A(href="#", cls="text-gray-500 hover:text-white transition-colors")("Terms of Service"),
                    A(href="#", cls="text-gray-500 hover:text-white transition-colors")("Cookie Policy")
                )
            )
        )
    )

    return (
        Title("InvoiceAI - Intelligent Invoice Parsing Solution"),
        header,
        hero,
        features_section,
        how_it_works,
        pricing_section,
        testimonials_section,
        faq_section,
        cta_section,
        footer
    )

serve()