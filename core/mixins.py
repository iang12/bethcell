# -*- coding: utf-8 -*-
from core.models import Celula, Evasao
from members.models import Leader,Discipulo
class DashboardMixin(object):
    #conta o total de lideres no banco.. 
    def get_context_data(self, **kwargs):
        context              = super(DashboardMixin, self).get_context_data(**kwargs)
        #is admin
        if self.request.user.is_superuser:
            context['lideres_count']    = Leader.objects.all().count()
            context['celulas_count']    = Celula.objects.all().count()
            context['discipulos_count'] = Discipulo.objects.all().count()
            context['evasao_count']     = Evasao.objects.all().count()

        else:
            leader = Leader.objects.get(user=self.request.user.pk,ministry='LG')
            context['lideres_count']     = Leader.objects.filter(lider_de_rede=leader).count()
            context['celulas_count']     = Celula.objects.filter(leader__lider_de_rede=leader).count()
            context['discipulos_count']  = Discipulo.objects.filter(leader__lider_de_rede=leader).count()
            context['evasao_count']      =  Evasao.objects.filter(leader__lider_de_rede=leader).count()
        return context
    
    #retorna os aniversariantes do dia..
    def aniversarios(self):
        today     = Leader.now().date()
        leader     = Lider.objects.filter(birth__day=today.day,birth_month=today.month).count()
        discipulo = Discipulo.objects.filter(birth__day=today.day,birth__month=today.month).count()
        return discipulo + leader
