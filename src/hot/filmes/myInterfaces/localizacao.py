from hot.filmes import _
from zope import schema
from zope.interface import Interface

# bibliotecas para otimizar busca
from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel.model import Schema
from zope.interface import alsoProvides

class Ilocalizacao(Schema):
    title = schema.TextLine(
        title       = _(u'Pais'),
        required    = True
    )
    cidade = schema.TextLine(
        title       = _(u'Cidade'),
        required    = True
    )
    sigla = schema.TextLine(
        title       = _(u'Sigla(estado/pais)'),
        description = _(u'abreviatura'),
        required    = False
    )
    # campo para pegar os subject do objeto
    tagsObj = schema.TextLine(
        required    = False,
        readonly    = True
    )
    dexteritytextindexer.searchable('cidade', 'title', 'sigla', 'tagsObj')

alsoProvides(Ilocalizacao, IFormFieldProvider)

    # campo com checkbox de uma escolha
    # <field name="type_of_talk" type="zope.schema.Choice"
    #   form:widget="z3c.form.browser.radio.RadioFieldWidget">
    #   <description />
    #   <title>Type of talk</title>
    #   <values>
    #     <element>Talk</element>
    #     <element>Training</element>
    #     <element>Keynote</element>
    #     <element>Lightning Talk</element>
    #   </values>
    # </field>
