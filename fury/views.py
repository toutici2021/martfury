from django.shortcuts import render

# Create your views here.

def home(request):
    datas= {

    }

    return render(request,'page/index.html',datas)

def page404(request):
    datas= {

    }

    return render(request,'page/404-page.html',datas)

def about(request):
    datas= {

    }

    return render(request,'page/about-us.html',datas)

def addresses(request):
    datas= {

    }

    return render(request,'user/addresses.html',datas)

def becomeavendor(request):
    datas= {

    }

    return render(request,'page/become-a-vendor.html',datas)

def checkout2(request):
    datas= {

    }

    return render(request,'page/checkout-2.html',datas)

def checkoutnew(request):
    datas= {

    }

    return render(request,'page/checkout-new.html',datas)

def checkout(request):
    datas= {

    }

    return render(request,'page/checkout.html',datas)

def commingsoon(request):
    datas= {

    }

    return render(request,'page/comming-soon.html',datas)

def compare(request):
    datas= {

    }

    return render(request,'page/compare.html',datas)

def contactus(request):
    datas= {

    }

    return render(request,'page/contact-us.html',datas)

def faqs(request):
    datas= {

    }

    return render(request,'page/faqs.html',datas)

def homemedical(request):
    datas= {

    }

    return render(request,'home/home-medical.html',datas)

def homepage2(request):
    datas= {

    }

    return render(request,'home/homepage-2.html',datas)



def homepage3(request):
    datas= {

    }

    return render(request,'home/homepage-3.html',datas)

def homepage4(request):
    datas= {

    }

    return render(request,'home/homepage-4.html',datas)

def homepage5(request):
    datas= {

    }

    return render(request,'home/homepage-5.html',datas)

def homepage6(request):
    datas= {

    }

    return render(request,'home/homepage-6.html',datas)

def homepage7(request):
    datas= {

    }

    return render(request,'home/homepage-7.html',datas)

def homepage8(request):
    datas= {

    }

    return render(request,'home/homepage-8.html',datas)

def homepage9(request):
    datas= {

    }

    return render(request,'home/homepage-9.html',datas)

def homepage10(request):
    datas= {

    }

    return render(request,'home/homepage-10.html',datas)

def homepagekids(request):
    datas= {

    }

    return render(request,'home/homepage-kids.html',datas)

def homepagephoto(request):
    datas= {

    }

    return render(request,'home/homepage-photo-and-video.html',datas)

#les views  payment et factures


def invoicedetail(request):
    datas= {

    }

    return render(request,'user/invoice-detail.html',datas)

def invoices(request):
    datas= {

    }

    return render(request,'user/invoices.html',datas)

def payment(request):
    datas= {

    }

    return render(request,'user/payment.html',datas)


def paymentsuccess(request):
    datas= {

    }

    return render(request,'user/payment-success.html',datas)

def notifications(request):
    datas= {

    }

    return render(request,'user/notifications.html',datas)

#les views de shop


def affiliate(request):
    datas={
        
    }
    return render(request, 'shop/affiliate.html')


def ordertracking(request):
    datas={
        
    }
    return render(request, 'shop/order-tracking.html')

def productaffiliate(request):
    datas={
        
    }
    return render(request, 'shop/product-affiliate.html')

def productbox(request):
    datas={
        
    }
    return render(request, 'shop/product-box.html')


def productcountdown(request):
    datas={
        
    }
    return render(request, 'shop/product-countdown.html')


def productdefault(request):
    datas={
        
    }
    return render(request, 'shop/product-default.html')


def productextend(request):
    datas={
        
    }
    return render(request, 'shop/product-extend.html')


def productfull(request):
    datas={
        
    }
    return render(request, 'shop/product-full-content.html')


def productgroup(request):
    datas={
        
    }
    return render(request, 'shop/product-groupped.html')


def productimage(request):
    datas={
        
    }
    return render(request, 'shop/product-image-swatches.html')


def productinsta(request):
    datas={
        
    }
    return render(request, 'shop/product-instagram.html')



def productmulti(request):
    datas={
        
    }
    return render(request, 'shop/product-multi-vendor.html')


def productonsale(request):
    datas={
        
    }
    return render(request, 'shop/product-on-sale.html')


def productout(request):
    datas={
        
    }
    return render(request, 'shop/product-out-stock.html')


def productsidebar(request):
    datas={
        
    }
    return render(request, 'shop/product-sidebar.html')



def productvideo(request):
    datas={
        
    }
    return render(request, 'shop/product-video.html')


def shipping(request):
    datas={
        
    }
    return render(request, 'shop/shipping.html')



def shopcaroussel(request):
    datas={
        
    }
    return render(request, 'shop/shop-carousel.html')



def shopcategorie(request):
    datas={
        
    }
    return render(request, 'shop/shop-categories.html')

def shopdef(request):
    datas={
        
    }
    return render(request, 'shop/shop-default.html')



def shopgrid(request):
    datas={
        
    }
    return render(request, 'shop/shop-grid.html')



def shopsidebarwhit(request):
    datas={
        
    }
    return render(request, 'shop/shop-sidebar-without-banner.html')



def shopsidebar(request):
    datas={
        
    }
    return render(request, 'shop/shop-sidebar.html')



def shoppingcart(request):
    datas={
        
    }
    return render(request, 'shop/shopping-cart.html')

def shopbrand(request):
    datas={
        
    }
    return render(request, 'shop/shopping-cart.html')




def whishlist(request):
    datas={
        
    }
    return render(request, 'shop/whishlist.html')




#les views de vendor 



def storedetailinfo(request):
    datas={
        
    }
    return render(request, 'vendor/store-detaili-nfo.html')



def storedetail(request):
    datas={
        
    }
    return render(request, 'vendor/store-detail.html')



def storelist(request):
    datas={
        
    }
    return render(request, 'vendor/store-list.html')

def storelist2(request):
    datas={
        
    }
    return render(request, 'vendor/store-list-2.html')



def vendorfree(request):
    datas={
        
    }
    return render(request, 'vendor/vendor-dashboard-free.html')



def vendorpro(request):
    datas={
        
    }
    return render(request, 'vendor/vendor-dashboard-pro.html')



def vendorstore(request):
    datas={
        
    }
    return render(request, 'vendor/vendor-store.html')


#les views de account

def account(request):
    datas={
        
    }
    return render(request, 'user/my-account.html')


def account2(request):
    datas={
        
    }
    return render(request, 'user/my-account-2.html')


def userinformation(request):
    datas={
        
    }
    return render(request, 'user/user-information.html')



