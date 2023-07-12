from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from application.models import (Introduction, SLogo, Activities, WorkShop, FAQLogo, FAQ, HeadLine,
                                ContactUs, Menu, SubMenu, SetLogo, SDhamLogo, TopHeaderText,
                                LeftSideTopBackground, RightBannerImages, OurTeam, Job, Shop)


def index(request):
    intro_dtl = Introduction.objects.values('introduction')
    
    head_line = HeadLine.objects.values('headLine')
    
    back_img = LeftSideTopBackground.objects.values('backgroundImage')

    img_right = RightBannerImages.objects.values('image')

    logo_str = SLogo.objects.values('sanImage')
   
    work_dtl = WorkShop.objects.values('workTitle')
    work_Img = WorkShop.objects.values('workImage')
    work_combined = [{'workTitle': act['workTitle'], 'workImage': img['workImage']} 
                    for act, img in zip(work_dtl, work_Img)]
    
    faqLogo = FAQLogo.objects.values('fLogo')
    
    question_dtl = FAQ.objects.values('question')
    answer_dtl = FAQ.objects.values('answer')
    faq_combined = [{'question': que['question'], 'answer': ans['answer']}
                     for que, ans in zip(question_dtl, answer_dtl)]
    
    telephone_dtl = ContactUs.objects.values('telephone')
    email_dtl = ContactUs.objects.values('email')
    address_dtl = ContactUs.objects.values('address')
    con_combined = [{'telephone': tel['telephone'], 'email': eml['email'], 'address': add['address']}
                     for tel, eml, add, in zip(telephone_dtl, email_dtl,address_dtl)]
                     
    # menu_name = Menu.objects.values('menuName')
    # url_menu = Menu.objects.values('url')
    # menu_combined = [{'menuName': menu['menuName'], 'url': url['url']}
    #                  for menu, url, in zip(menu_name,url_menu)]


    # sub_menu = SubMenu.objects.values('menu')
    # submenu = SubMenu.objects.values('submenu')
    # sub_url = SubMenu.objects.values('url')
    # submenu_combined = [{'menu': menu['menu'], 'submenu': sub['submenu'], 'url': url['url']}
    #                  for menu, sub, url, in zip(sub_menu, submenu, sub_url)]
    
    
    activities = Activities.objects.values('activities')
    sImage1 = Activities.objects.values('smallImage1') 
    sImage2 = Activities.objects.values('smallImage2') 
    lImage = Activities.objects.values('largeImage') 
    sImage3 = Activities.objects.values('smallImage3') 
    sImage4 = Activities.objects.values('smallImage4') 
        
    act_comb = [{'activities': act['activities'], 'smallImage1': sim1['smallImage1'], 'smallImage2': sim2['smallImage2'],
                 'largeImage': lim['largeImage'], 'smallImage3': sim3['smallImage3'],'smallImage4':sim4['smallImage4']}
                     for act, sim1, sim2, lim, sim3, sim4 in 
                     zip(activities, sImage1, sImage2, lImage, sImage3, sImage4)] 
    
    
    ourteams = OurTeam.objects.all()
    team_data = []

    for ourteam in ourteams:
        jobs = Job.objects.filter(jobname=ourteam)
        job_data = []

        for job in jobs:
            job_data.append({
                'timage': job.timage,
                'name': job.name,
                'designation': job.designation,
                'remark': job.remark
            })

        team_data.append({
            'jobname': ourteam.teamname,
            'jobs': job_data
        })

    

    # o_name = Mentor.objects.values('name')
    # o_design = Mentor.objects.values('designation') 
    # o_remark = Mentor.objects.values('remark')
    # o_timge = Mentor.objects.values('timage')
    
    # Team_comb = [{'name': nam['name'], 'designation': des['designation'],
    #               'remark': rem['remark'], 'timage': tim['timage']} 
    #             for nam, des, rem, tim in zip(o_name, o_design, o_remark, o_timge)]   
    
    # ourteams = OurTeam.objects.all()
    # team_data = []
    # for ourteam in ourteams:
    #     jobs = Job.objects.filter(jobname=ourteam)
    #     job_timage = [jobimage.timage for jobimage in jobs]
        
    #     jobsnm = Job.objects.filter(jobname=ourteam)
    #     job_name = [jobnm.name for jobnm in jobsnm]
        
    #     jobsde = Job.objects.filter(jobname=ourteam)
    #     job_desgn = [jobdesgn.designation for jobdesgn in jobsde]
        
    #     jobsrm = Job.objects.filter(jobname=ourteam)
    #     job_remark = [job_remark.remark for job_remark in jobsrm]
    #     team_data.append({'jobname': ourteam.teamname, 'jobs':job_timage, 'jobsnm': job_name,
    #                       'jobsde':job_desgn, 'jobsrm':job_remark })
                        
    
    
    
    menus = Menu.objects.all()
    menu_data = []
    for menu in menus:
        submenus = SubMenu.objects.filter(menu=menu)
        submenu_data = [submenu.submenu for submenu in submenus]
        menu_data.append({'menu': menu.menuName, 'submenus': submenu_data, 'url': menu.url})
    
    set_logo = SetLogo.objects.values('setLogo')
    
    dha_logo = SDhamLogo.objects.values('dhaLogo')
    
    head_title = TopHeaderText.objects.values('title')
    head_tlLogo = TopHeaderText.objects.values('tlLogo') 
    head_comb = [{'title': ttl['title'], 'tlLogo': tlg['tlLogo']}
                     for ttl, tlg in zip(head_title, head_tlLogo)]
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        
        send_mail(
            'New Comment',
            f'Name: {name}\nEmail: {email}\nComment: {comment}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        # Redirect or render a success message 
        return render(request, 'success.html')
    
    return render(request, 'index.html', {'index': intro_dtl, 'index1': logo_str,'back_img':back_img,
                                           'work_combined': work_combined, 'faq_combined':faq_combined,
                                           'faqLogo':faqLogo, 'con_combined': con_combined, 'set_logo':set_logo,
                                           'menu_data': menu_data, 'dha_logo':dha_logo, 'head_title':head_title,
                                           'head_comb':head_comb, 'head_line':head_line, 'img_right':img_right,
                                           'act_comb':act_comb, 'team_data':team_data})




# def comment_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         comment = request.POST.get('comment')
        
#         send_mail(
#             'New Comment',
#             f'Name: {name}\nEmail: {email}\nComment: {comment}',
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.DEFAULT_FROM_EMAIL],
#             fail_silently=False,
#         )
#         # Redirect or render a success message 
#         return render(request, 'success.html')
        
#     return render(request, 'comment_form.html')

def calender(request):
    set_logo = SetLogo.objects.values('setLogo')
    
    dha_logo = SDhamLogo.objects.values('dhaLogo')
    
    head_title = TopHeaderText.objects.values('title')
    head_tlLogo = TopHeaderText.objects.values('tlLogo') 
    head_comb = [{'title': ttl['title'], 'tlLogo': tlg['tlLogo']}
                     for ttl, tlg in zip(head_title, head_tlLogo)]
    
    menus = Menu.objects.all()
    menu_data = []
    for menu in menus:
        submenus = SubMenu.objects.filter(menu=menu)
        submenu_data = [submenu.submenu for submenu in submenus]
        menu_data.append({'menu': menu.menuName, 'submenus': submenu_data, 'url': menu.url})
    
    return render(request, 'calender.html', {"set_logo":set_logo, "dha_logo":dha_logo, "head_comb":head_comb,
                                             "menu_data":menu_data})

def shop(request):

    proimg = Shop.objects.values('proLogo')
    proname = Shop.objects.values('productName')
    prors = Shop.objects.values('rs')
    pro_comb = [{'proLogo': pri['proLogo'], 'productName': prn['productName'], 'rs': prs['rs']}
              for pri, prn, prs in zip(proimg, proname, prors)]
    
    menus = Menu.objects.all()
    menu_data = []
    for menu in menus:
        submenus = SubMenu.objects.filter(menu=menu)
        submenu_data = [submenu.submenu for submenu in submenus]
        menu_data.append({'menu': menu.menuName, 'submenus': submenu_data, 'url': menu.url})
    
    set_logo = SetLogo.objects.values('setLogo')
    
    dha_logo = SDhamLogo.objects.values('dhaLogo')
    
    head_title = TopHeaderText.objects.values('title')
    head_tlLogo = TopHeaderText.objects.values('tlLogo') 
    head_comb = [{'title': ttl['title'], 'tlLogo': tlg['tlLogo']}
                     for ttl, tlg in zip(head_title, head_tlLogo)]
    
    head_line = HeadLine.objects.values('headLine')
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        
        send_mail(
            'New Comment',
            f'Name: {name}\nEmail: {email}\nComment: {comment}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        # Redirect or render a success message 
        return render(request, 'success.html')
    
    return render(request, 'shop.html', {'pro_comb':pro_comb, 'menu_data': menu_data, 'dha_logo':dha_logo,
                                         'set_logo':set_logo, 'head_comb':head_comb,'head_line':head_line})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired homepage URL name
        else:
            error_message = "Invalid login credentials"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with your login URL name
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def test(request):

    proimg = Shop.objects.values('proLogo')
    proname = Shop.objects.values('productName')
    prors = Shop.objects.values('rs')
    pro_comb = [{'proLogo': pri['proLogo'], 'productName': prn['productName'], 'rs': prs['rs']}
              for pri, prn, prs in zip(proimg, proname, prors)]
    
    menus = Menu.objects.all()
    menu_data = []
    for menu in menus:
        submenus = SubMenu.objects.filter(menu=menu)
        submenu_data = [submenu.submenu for submenu in submenus]
        menu_data.append({'menu': menu.menuName, 'submenus': submenu_data, 'url': menu.url})
    
    set_logo = SetLogo.objects.values('setLogo')
    
    dha_logo = SDhamLogo.objects.values('dhaLogo')
    
    head_title = TopHeaderText.objects.values('title')
    head_tlLogo = TopHeaderText.objects.values('tlLogo') 
    head_comb = [{'title': ttl['title'], 'tlLogo': tlg['tlLogo']}
                     for ttl, tlg in zip(head_title, head_tlLogo)]
    
    head_line = HeadLine.objects.values('headLine')
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        
        send_mail(
            'New Comment',
            f'Name: {name}\nEmail: {email}\nComment: {comment}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        # Redirect or render a success message 
        return render(request, 'success.html')
    
    return render(request, 'test.html', {'pro_comb':pro_comb, 'menu_data': menu_data, 'dha_logo':dha_logo,
                                         'set_logo':set_logo, 'head_comb':head_comb,'head_line':head_line})
    
    
def master(request):
    proimg = Shop.objects.values('proLogo')
    proname = Shop.objects.values('productName')
    prors = Shop.objects.values('rs')
    pro_comb = [{'proLogo': pri['proLogo'], 'productName': prn['productName'], 'rs': prs['rs']}
              for pri, prn, prs in zip(proimg, proname, prors)]
    
    menus = Menu.objects.all()
    menu_data = []
    for menu in menus:
        submenus = SubMenu.objects.filter(menu=menu)
        submenu_data = [submenu.submenu for submenu in submenus]
        menu_data.append({'menu': menu.menuName, 'submenus': submenu_data, 'url': menu.url})
    
    set_logo = SetLogo.objects.values('setLogo')
    
    dha_logo = SDhamLogo.objects.values('dhaLogo')
    
    head_title = TopHeaderText.objects.values('title')
    head_tlLogo = TopHeaderText.objects.values('tlLogo') 
    head_comb = [{'title': ttl['title'], 'tlLogo': tlg['tlLogo']}
                     for ttl, tlg in zip(head_title, head_tlLogo)]
    
    head_line = HeadLine.objects.values('headLine')
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        
        send_mail(
            'New Comment',
            f'Name: {name}\nEmail: {email}\nComment: {comment}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        # Redirect or render a success message 
        return render(request, 'success.html')
    
    return render(request, 'master.html', {'pro_comb':pro_comb, 'menu_data': menu_data, 'dha_logo':dha_logo,
                                         'set_logo':set_logo, 'head_comb':head_comb,'head_line':head_line})
    
    