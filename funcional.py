"""
Semana 3 — Reescrevendo com programação funcional

Funções puras, imutabilidade, map, filter, sorted e lambda.
"""

from collections import namedtuple

ALIQUOTA_PADRAO = 0.25

ALIQUOTAS = {"cesta_basica": 0.0, "reduzido": 0.10, "padrao": 0.25}

Item = namedtuple("Item", ["nome", "preco", "categoria", "quantidade"], defaults=[1])


def aliquota(categoria):
    """Retorna a alíquota da categoria. ValueError se ela não existir."""
    if categoria not in ALIQUOTAS:
        raise ValueError(f"Categoria desconhecida: {categoria}")
    return ALIQUOTAS[categoria]


def imposto_item(item):
    """Imposto do item: round(round(preco * aliquota, 2) * quantidade, 2)."""
    return round(round(item.preco * aliquota(item.categoria), 2) * item.quantidade, 2)


def total_impostos(itens):
    """Soma dos impostos de todos os itens."""
    return round(sum(map(imposto_item, itens)), 2)


def total_compra(itens):
    """Soma de preco * quantidade de todos os itens, mais os impostos."""
    subtotal = sum(map(lambda item: item.preco * item.quantidade, itens))
    return round(subtotal + total_impostos(itens), 2)


def filtrar_por_categoria(itens, categoria):
    """Lista nova apenas com os itens da categoria."""
    return list(filter(lambda item: item.categoria == categoria, itens))


def ordenar_por_preco(itens, decrescente=False):
    """Lista nova ordenada pelo preço unitário."""
    return sorted(itens, key=lambda item: item.preco, reverse=decrescente)


def economia_total(itens):
    """Quanto a mais seria pago se todos os itens tivessem a alíquota padrão."""
    imposto_se_padrao = sum(
        map(
            lambda item: round(item.preco * ALIQUOTA_PADRAO, 2) * item.quantidade,
            itens,
        )
    )
    return round(imposto_se_padrao - total_impostos(itens), 2)
