from django.urls import path
from fury import views


urlpatterns = [

    path('', views.home, name='home'),
    path('page404', views.page404, name='page404'),
    path('about', views.about, name='about'),
    path('addresses', views.addresses, name='addresses'),
    path('becomeavendor', views.becomeavendor, name='becomeavendor'),
    path('checkout2', views.checkout2, name='checkout2'),
    path('checkoutnew', views.checkoutnew, name='checkoutnew'),
    path('checkout', views.checkout, name='checkout'),
    path('commingsoon', views.commingsoon, name='commingsoon'),
    path('compare', views.compare, name='compare'),
    path('contactus', views.contactus, name='contactus'),
    path('faqs', views.faqs, name='faqs'),
    path('homemedical', views.homemedical, name='homemedical'),
    path('homepage2', views.homepage2, name='homepage2'),
    path('homepage3', views.homepage3, name='homepage3'),
    path('homepage4', views.homepage4, name='homepage4'),
    path('homepage5', views.homepage5, name='homepage5'),
    path('homepage6', views.homepage6, name='homepage6'),
    path('homepage7', views.homepage7, name='homepage7'),
    path('homepage8', views.homepage8, name='homepage8'),
    path('homepage9', views.homepage9, name='homepage9'),
    path('homepage10', views.homepage10, name='homepage10'),
    path('homepagekids', views.homepagekids, name='homepagekids'),
    path('homepagephoto', views.homepagephoto, name='homepagephoto'),

      #les urls de shop


    path('affiliate',views.affiliate,name='affiliate'),
    path('ordertracking',views.ordertracking,name='ordertracking'),
    path('productaffiliate',views.productaffiliate,name='productaffiliate'),
    path('productbox',views.productbox,name='productbox'),
    path('productcountdown',views.productcountdown,name='productcountdown'),
    path('productdefault',views.productdefault,name='productdefault'),
    path('productextend',views.productextend,name='productextend'),
    path('productfull',views.productfull,name='productfull'),
    path('productgroup',views.productgroup,name='productgroup'),
    path('productimage',views.productimage,name='productimage'),
    path('productinsta',views.productinsta,name='productinsta'),
    path('productmulti',views.productmulti,name='productmulti'),
    path('productonsale',views.productonsale,name='productonsale'),
    path('productout',views.productout,name='productout'),
    path('productsidebar',views.productsidebar,name='productsidebar'),
    path('productvideo',views.productvideo,name='productvideo'),
    path('shipping',views.shipping,name='shipping'),
    path('shopcaroussel',views.shopcaroussel,name='shopcaroussel'),
    path('shopcategorie',views.shopcategorie,name='shopcategorie'),
    path('shopdef',views.shopdef,name='shopdef'),
    path('shopgrid',views.shopgrid,name='shopgrid'),
    path('shopsidebarwhit',views.shopsidebarwhit,name='shopsidebarwhit'),
    path('shopsidebar',views.shopsidebar,name='shopsidebar'),
    path('shoppingcart',views.shoppingcart,name='shoppingcart'),
    path('whishlist',views.whishlist,name='whishlist'),
    path('shopbrand',views.shopbrand,name='shopbrand'),


#les urls de vendor 

    path('storedetailinfo',views.storedetailinfo,name='storedetailinfo'),
    path('storedetail',views.storedetail,name='storedetail'),
    path('storelist',views.storelist,name='storelist'),
    path('storelist2',views.storelist2,name='storelist2'),
    path('vendorfree',views.vendorfree,name='vendorfree'),
    path('vendorpro',views.vendorpro,name='vendorpro'),
    path('vendorstore',views.vendorstore,name='vendorstore'),


#les urls account 


    path('account',views.account,name='account'),
    path('account2',views.account2,name='account2'),
    path('userinformation',views.userinformation,name='userinformation'),


    


#les urls payements et factures

    path('paymentsuccess',views.paymentsuccess,name='paymentsuccess'),
    path('payment',views.payment,name='payment'),
    path('notifications',views.notifications,name='notifications'),
    path('invoicedetail', views.invoicedetail, name='invoicedetail'),
    path('invoices', views.invoices, name='invoices'),

]