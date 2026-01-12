from django.urls import path, include
from . import views

app_name = 'Ouvidoria'

urlpatterns = [
    # Analisador de Transgressões parte principal do projeto index
    path('', views.index, name='index'),  

    # Aba de efetivos
    path('efetivo/', views.MilitarListView.as_view(), name='militar_list'),
    path('militar/<int:pk>/patds/', views.MilitarPATDListView.as_view(), name='militar_patd_list'),
    path('militar/<int:pk>/', views.MilitarDetailView.as_view(), name='militar_detail'),

    # Aba de PATDs
    path('patd/', views.PATDListView.as_view(), name='patd_list'),
    path('patd/finalizadas/', views.PatdFinalizadoListView.as_view(), name='patd_finalizado_list'),
    path('minhas-atribuicoes/', views.patd_atribuicoes_pendentes, name='patd_atribuicoes_pendentes'),
    path('patd/<int:pk>/', views.PATDDetailView.as_view(), name='patd_detail'),
    path('patd/<int:pk>/editar/', views.PATDUpdateView.as_view(), name='patd_update'),
    path('patd/<int:pk>/excluir/', views.PATDDeleteView.as_view(), name='patd_delete'),
    path('patd/<int:pk>/salvar_assinatura/', views.salvar_assinatura, name='salvar_assinatura'),
    path('patd/<int:pk>/salvar_documento/', views.salvar_documento_patd, name='salvar_documento_patd'),
    path('patd/<int:pk>/salvar_assinatura_ciencia/', views.salvar_assinatura_ciencia, name='salvar_assinatura_ciencia'),
    path('patd/<int:pk>/salvar_alegacao_defesa/', views.salvar_alegacao_defesa, name='salvar_alegacao_defesa'),
    path('patd/<int:pk>/salvar_assinatura_defesa/', views.salvar_assinatura_defesa, name='salvar_assinatura_defesa'),
    path('patd/<int:pk>/salvar_assinatura_reconsideracao/', views.salvar_assinatura_reconsideracao, name='salvar_assinatura_reconsideracao'),
    path('patd/<int:pk>/extender_prazo/', views.extender_prazo, name='extender_prazo'),
    path('patd/<int:pk>/prosseguir_sem_alegacao/', views.prosseguir_sem_alegacao, name='prosseguir_sem_alegacao'), 
    path('patd/<int:pk>/salvar_assinatura_testemunha/<int:testemunha_num>/', views.salvar_assinatura_testemunha, name='salvar_assinatura_testemunha'),
    path('patd/<int:pk>/atribuir_oficial/', views.atribuir_oficial, name='atribuir_oficial'),
    path('patd/<int:pk>/aceitar_atribuicao/', views.aceitar_atribuicao, name='aceitar_atribuicao'),
    path('patd/<int:pk>/justificar/', views.justificar_patd, name='justificar_patd'),
    path('patd/<int:pk>/finalizar/', views.finalizar_publicacao, name='finalizar_publicacao'),
    path('patd/<int:pk>/salvar_nova_punicao/', views.salvar_nova_punicao, name='salvar_nova_punicao'),

    path('patds/<int:pk>/regenerar-ocorrencia/', views.regenerar_ocorrencia, name='regenerar_ocorrencia'),
    path('patds/<int:pk>/regenerar-resumo-defesa/', views.regenerar_resumo_defesa, name='regenerar_resumo_defesa'),
    path('patds/<int:pk>/regenerar-texto-relatorio/', views.regenerar_texto_relatorio, name='regenerar_texto_relatorio'),
    path('patds/<int:pk>/regenerar-punicao/', views.regenerar_punicao, name='regenerar_punicao'),

    path('patd/<int:pk>/exportar-docx/', views.exportar_patd_docx, name='exportar_patd_docx'),



    # --- ROTAS DE ANÁLISE E APURAÇÃO ---
    path('patd/<int:pk>/analisar_punicao/', views.analisar_punicao, name='analisar_punicao'),
    path('patd/<int:pk>/salvar_apuracao/', views.salvar_apuracao, name='salvar_apuracao'), 
    path('patd/<int:pk>/avancar_para_comandante/', views.avancar_para_comandante, name='avancar_para_comandante'),

    # ROTAS PARA O COMANDANTE
    path('comandante/dashboard/', views.ComandanteDashboardView.as_view(), name='comandante_dashboard'),
    path('patd/<int:pk>/aprovar/', views.patd_aprovar, name='patd_aprovar'),
    path('patd/<int:pk>/retornar/', views.patd_retornar, name='patd_retornar'),
    path('patd/<int:pk>/solicitar_reconsideracao/', views.solicitar_reconsideracao, name='solicitar_reconsideracao'),
    path('patd/<int:pk>/salvar_reconsideracao/', views.salvar_reconsideracao, name='salvar_reconsideracao'),
    path('patd/<int:pk>/anexar_reconsideracao_oficial/', views.anexar_documento_reconsideracao_oficial, name='anexar_reconsideracao_oficial'),


    # CONFIGURAÇÃO DE ASSINATURAS
    path('config/oficiais/', views.lista_oficiais, name='lista_oficiais'),
    path('militar/<int:pk>/salvar_assinatura_padrao/', views.salvar_assinatura_padrao, name='salvar_assinatura_padrao'),
    path('config/padroes/', views.gerenciar_configuracoes_padrao, name='gerenciar_configuracoes_padrao'),

    # ROTAS PARA NOTIFICAÇÕES
    path('notificacoes/patds-expirados/', views.patds_expirados_json, name='patds_expirados_json'),
    path('notificacoes/atribuicoes-pendentes/', views.patd_atribuicoes_pendentes_json, name='patd_atribuicoes_pendentes_json'),
    path('notificacoes/comandante-pendencias/', views.comandante_pendencias_json, name='comandante_pendencias_json'),
    path('notificacoes/extender-prazo-massa/', views.extender_prazo_massa, name='extender_prazo_massa'),
    path('notificacoes/verificar-prazos/', views.verificar_e_atualizar_prazos, name='verificar_e_atualizar_prazos'),

    # API
    path('api/search-militares/', views.search_militares_json, name='search_militares_json'),
    path('anexo/<int:pk>/excluir/', views.excluir_anexo, name='excluir_anexo'),
]
