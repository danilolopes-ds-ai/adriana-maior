# Adriana Maior — Site de Geobiologia & Radiestesia

## 📁 Estrutura do Projeto

```
adriana-maior/
├── index.html              ← Página principal (HTML semântico)
├── css/
│   ├── design-system.css   ← Tokens de cores, tipografia, botões, reset
│   └── pages.css           ← Componentes: header, hero, cards, animations
├── js/
│   └── main.js             ← Mobile nav, header scroll, scroll reveal
├── assets/
│   └── img/                ← Pasta para imagens (JPG, PNG, WebP)
├── README.md               ← Este arquivo
├── .cursorrules            ← Instruções para Copilot
├── designer-system.md      ← Documentação do Design System (Remedy Place)
└── .gitignore              ← Arquivos a ignorar no Git
```

---

## 🎨 Design System

**Referência:** RemedyPlace.com — Luxo Minimalista/Editorial

### Paleta de Cores
- `--onyx` (#1a1817) — Background principal
- `--earth-light` (#4b443c) — Cards, elementos secundários
- `--bone` (#b9b2aa) — Texto principal
- `--air` (#edecea) — Headings

### Tipografia
- **Display:** Cormorant Garamond (Serif)
- **Body/UI:** Inter (Sans-serif)

### Componentes
- ✨ **Hero with CTA** — Full-screen com vignette radial
- 🏷️ **Service Cards** — Bento Grid 3 colunas
- 🔘 **Botões** — Ghost, Secondary, Primary
- 📱 **Mobile Nav** — Menu responsivo com animação

---

## 🚀 Funcionalidades JavaScript

### `js/main.js`
1. **Mobile Navigation** — Menu hamburguês com overlay responsivo
2. **Header Scroll Effect** — Background blur ao scrolar
3. **Scroll Reveal** — Animações ao entrar na viewport (Intersection Observer)
4. **Smooth Scroll** — Navegação suave para âncoras
5. **Button Animations** — Micro-interações de hover
6. **Lazy Loading** — Carregamento preguiçoso de imagens

---

## 📝 HTML Semântico

- `<header>`, `<nav>`, `<section>`, `<article>` 
- Classes BEM para modularidade
- Atributos `data-*` para JavaScript
- Acessibilidade WCAG AA

---

## 🔗 Third-party CDNs

- **Tailwind CSS** — Framework CSS
- **Google Fonts** — Cormorant Garamond + Inter

---

## 📱 Responsivo

- **Mobile-first** approach
- Breakpoints: 640px (sm), 768px (md), 1024px (lg), 1920px (2xl)
- Tipografia fluida com `clamp()`
- Imagens otimizadas

---

## 🎯 Próximos Passos

- [ ] Integrar foto da Adriana com filtro de saturação
- [ ] Seção de Depoimentos/Casos de Sucesso
- [ ] Formulário de Contato/Agendamento
- [ ] Blog de Artigos
- [ ] Footer com Links + Newsletter
- [ ] SEO optimization (meta tags, schema.org)
- [ ] Analytics (Google Analytics)

---

## 📄 Licença

Projeto privado — Adriana Maior. Todos os direitos reservados.

---

**Desenvolvido com ❤️ — Português do Brasil obrigatório!**
