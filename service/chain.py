from service.handler import *

_handlers = [
    CpfHandler(),
    NomeHandler(),
    SexoHandler(),
    AdminHandler(),
    DataNascimentoHandler(),
    PosicaoHandler(),
    ConteudoHandler(),
    EstadoIdHandler(),
    SenhaHandler(),
    CargoIdHandler(),
    CepHandler(),
    AreaIdHandler(),
    ZonaIdHandler(),
    PolicialIdHandler(),
    SetorIdHandler(),
    CreatedAtHandler(),
    DataInicioHandler(),
    DataFimHandler(),
    JustificativaHandler(),
    CpfVitimaHandler(),
    UpdatedAtHandler(),
    CidadeHandler(),
    CreatedByHandler(),
    UpdatedByHandler(),
    TipoIdHandler(),
    BoIdHandler(),
]

for atual, proximo in zip(_handlers, _handlers[1:]):
    atual.set_next(proximo)

chain = _handlers[0]

