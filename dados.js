// Tudo que aparece no contrato vem daqui. Edite à vontade.
// Datas no formato AAAA-MM-DD.
window.DADOS = {
  partes: {
    contratante: { nome: "Juan Luccas G. Razzano", apelido: "Juan" },
    contratada: { nome: "Carolina Yukie Horita", apelido: "Chorita" },
  },

  marcos: [
    { data: "2026-05-23", titulo: "Primeira conversa", texto: "Início das tratativas." },
    { data: "2026-06-25", titulo: "Primeiro encontro", texto: "Primeira reunião presencial. Resultado: nova reunião agendada." },
    { data: "2026-09-14", titulo: "Primeiro “eu te amo”", texto: "Declaração feita e recebida. Irrevogável." },
  ],

  requisitos: [
    { texto: "Gostar de bala de leite" },
    { texto: "Ter uma música de conforto", nota: "“A Horse with No Name”, America (1971)." },
    { texto: "Topar foto em qualquer espelho", nota: "Inclusive de ônibus." },
    { texto: "Fazer careta na hora da foto", nota: "Comprovado por farto material fotográfico." },
    { texto: "Topar fantasia combinando", nota: "Ver Anexo I." },
    { texto: "Saber escolher jabuticaba" },
  ],

  beneficios: [
    { titulo: "Bala de leite", texto: "Fornecimento contínuo. Reposição em até 24 horas após o fim do estoque." },
    { titulo: "Flores", texto: "Lírios e tulipas, sem necessidade de data comemorativa." },
    { titulo: "Frutas", texto: "Jabuticaba e mexerica durante a safra. Mexerica entregue descascada." },
    { titulo: "Trilha sonora", texto: "Acesso irrestrito a “A Horse with No Name”, inclusive no trânsito." },
    { titulo: "Refeições", texto: "Rodízio entre os estabelecimentos do Anexo II e novos a descobrir, com direito de veto da contratada." },
  ],

  diaADia: [
    "Escolher o restaurante em regime de alternância, com direito de veto da contratada.",
    "Registrar em foto todo espelho relevante encontrado no caminho.",
    "Responder careta com careta.",
    "Dividir a sobremesa em partes iguais, salvo acordo em contrário.",
    "Avisar quando chegar em casa.",
  ],

  // Anexo II. "tipo" vira a categoria do gráfico. "data" é opcional (AAAA-MM-DD).
  lugares: [
    { nome: "Holy Burger", tipo: "Lanches", data: "2026-09-02" },
    { nome: "Merenda da Cidade", tipo: "Brasileira", data: "2026-09-19" },
    { nome: "Baeta Bar", tipo: "Bar" },
    { nome: "Cinema", tipo: "Cinema" },
    { nome: "Rong He", tipo: "Asiática" },
    { nome: "Pizzaria da Mooca", tipo: "Italiana" },
    { nome: "Espaço Kazu", tipo: "Asiática" },
    { nome: "Cangote", tipo: "Sorveteria" },
    { nome: "Copanzinho", tipo: "Bar" },
    { nome: "Mercadão", tipo: "Brasileira" },
    { nome: "Zé Bolinho", tipo: "Lanches" },
    { nome: "Zdeli", tipo: "Lanches" },
    { nome: "La Pasta Gialla", tipo: "Italiana" },
    { nome: "Ó Pro Cê Vê", tipo: "Bar" },
    { nome: "Prainha", tipo: "Brasileira" },
  ],

  // Anexo III. "genero" alimenta o gráfico; "pais" também.
  filmes: [
    { titulo: "Resident Evil", ano: 2026, genero: "Terror", sub: "Zumbis", pais: "EUA" },
    { titulo: "A Hora do Mal (Weapons)", ano: 2025, genero: "Terror", sub: "Mistério", pais: "EUA" },
    { titulo: "Bacurau", ano: 2019, genero: "Faroeste", sub: "Ficção científica", pais: "Brasil" },
    { titulo: "Extermínio: A Evolução (28 Years Later)", ano: 2025, genero: "Terror", sub: "Infectados", pais: "Reino Unido" },
    { titulo: "A Substância (The Substance)", ano: 2024, genero: "Terror", sub: "Horror corporal", pais: "França" },
    { titulo: "Forbidden Fruits", ano: 2026, genero: "Terror", sub: "Comédia de terror", pais: "EUA" },
    { titulo: "Sorria (Smile)", ano: 2022, genero: "Terror", sub: "Sobrenatural", pais: "EUA" },
    { titulo: "Quando o Mal Espreita (When Evil Lurks)", ano: 2023, genero: "Terror", sub: "Possessão", pais: "Argentina" },
    { titulo: "Obsession", ano: 2026, genero: "Terror", sub: "Psicológico", pais: "EUA" },
    { titulo: "Casamento Sangrento (Ready or Not)", ano: 2019, genero: "Terror", sub: "Comédia de terror", pais: "EUA" },
    { titulo: "Oldboy", ano: 2003, genero: "Suspense", sub: "Vingança", pais: "Coreia do Sul" },
  ],
  series: [
    { titulo: "O Verão que Mudou Minha Vida", ano: "2022–2025", genero: "Romance", pais: "EUA", status: "Concluída" },
    { titulo: "Emergência 53", ano: "2026", genero: "Drama médico", pais: "Brasil", status: "Em andamento" },
  ],

  vigencia: "Prazo indeterminado, renovado automaticamente a cada dia. Alterações somente por acordo entre as partes.",
};
