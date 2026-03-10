# Design System — Remedy Place

---

## 1. Identidade Visual

**Conceito:** *Wellness de luxo* — dark mode elegante, tons terrosos quentes, minimalismo sofisticado. A estética é sóbria, orgânica e premium, remetendo a spas exclusivos.

---

## 2. Paleta de Cores

| Token | Nome | HEX | RGB | Uso |
|---|---|---|---|---|
| `bg-onyx` | **Onyx** | `#1a1817` | rgb(26, 24, 23) | Background principal |
| `--footer-bg` | **Onyx Dark** | `#141210` | rgb(20, 18, 16) | Background do footer |
| `bg-earthLight` | **Earth Light** | `#4b443c` | rgb(75, 68, 60) | Backgrounds secundários, bordas ativas |
| `text-bone` / `bg-bone` | **Bone** | `#b9b2aa` | rgb(185, 178, 170) | Texto principal, ícones, nav links |
| `border-bone` | **Bone Light** | `#cdc9c2` | rgb(205, 201, 194) | Bordas, botão CTA hero |
| `text-air` / linen | **Air/Linen** | `#edecea` | rgb(237, 236, 234) | Headings principais (H1, H3) |
| `text-air` dark | **Earth Dark** | `#30251c` | rgb(48, 37, 28) | Texto sobre fundos claros, badges |
| `--banner-bg` | **Linen Semi-transparente** | `#fdfaf1` @ 80% | rgba(253, 250, 241, 0.8) | Barra de anúncio (topo) |

**Esquema de cor:** Monocromático quente escuro (dark palette) com tons de bege/terra.

---

## 3. Tipografia

### Famílias de Fonte

| Família | Uso | Variante |
|---|---|---|
| **Beausite Slick** | Headings (H1–H3), display | Fonte primária de display |
| **Beausite Classic** | Body, botões, labels, nav, UI | Fonte secundária funcional |
| `ui-sans-serif` (fallback) | Sistema | Fallback genérico |

### Escala Tipográfica

| Tag | Fonte | Tamanho | Peso | Line-height | Letter-spacing | Transform | Cor |
|---|---|---|---|---|---|---|---|
| **H1** | Beausite Slick | 30px | 400 | 1.0 (30px) | normal | UPPERCASE | Air `#edecea` |
| **H2 — Display** | Beausite Slick | 30px | 400 | 36px | normal | UPPERCASE | Bone `#b9b2aa` |
| **H2 — Section** | Beausite Slick | 24px | 300–400 | 28.8px | normal | none / UPPERCASE | Bone `#b9b2aa` |
| **H3** | Beausite Slick | 16px | 400 | 19.2px | normal | UPPERCASE | Air `#edecea` |
| **H4 — Label** | Beausite Classic | 12px | 500 | 14.4px | 0.96px (0.08em) | UPPERCASE | Earth Dark `#30251c` |
| **H4 — Location** | Beausite Classic | 14px | 400 | 16.8px | 0.35px | UPPERCASE | Bone `#b9b2aa` |
| **Body / Parágrafo** | Beausite Classic | 16px | 400 | 24px (1.5) | normal | none | Bone `#b9b2aa` |
| **Body light** | Beausite Classic | 16px | 300 | 24px | 0.4px | none | Air `#edecea` |
| **Small / Caption** | Beausite Classic | 14px | 400 | 16.8px | normal | none | Bone `#b9b2aa` |
| **Micro / Badge** | Beausite Classic | 12px | 400–500 | 14.4px | 0.96–1.2px | UPPERCASE | variável |
| **Footer Label** | Beausite Classic | 14px | 700 | 16.8px | normal | none | Bone `#b9b2aa` |

**Padrão predominante:** Letter-spacing expandido (0.35–1.6px) + UPPERCASE em todos os elementos de UI → sensação de luxo/spa.

---

## 4. Botões

### Button — CTA Hero (Primary)

```
Componente: .hero-with-cta__button .button .border-bone .text-bone
Fonte: Beausite Classic, 14px, weight 400
Cor do texto: #1a1817 (Onyx) — invertido sobre fundo claro
Background: #cdc9c2 (Bone Light)
Border: 1px solid #cec9c2
Border-radius: 0px (sem arredondamento)
Padding: 20px 24px (py-5 px-6)
Letter-spacing: 1.4px
Transform: UPPERCASE
Display: inline-flex
Width: 260px (normalizada)
```

### Button — Navigation / List Item

```
Componente: .button .button-size-short
Fonte: Beausite Classic, 14px, weight 400
Cor do texto: #b9b2aa (Bone)
Background: transparent
Border: 1px solid Earth Light (#4b443c) — top, bottom, side borders
Border-radius: 0px
Padding: 0 40px
Letter-spacing: 1.4px
Transform: UPPERCASE
```

**Padrão visual de botões:** Sem border-radius, borda sutil, texto uppercase com alto letter-spacing → estilo editorial/minimalista.

---

## 5. Inputs / Formulários

```
Fonte: Beausite Classic, 14px
Cor do texto: Bone (#b9b2aa)
Background: transparente
Border: 1px solid rgba(93, 92, 92, 0.5)
Border-radius: 0px
Padding-left: 16px
Outline: none
Placeholder: "Email Address"
```

---

## 6. Componentes UI

### Site Banner (`.site-banner`)
- Background: `#fdfaf1` @ 80% opacity (Linen semi-transparente)
- Posição: fixed top, z-index 30
- Border-bottom: 1px
- Padding: `px-10` (40px horizontal), `md:px-6`
- Texto: Beausite Classic, 12px, uppercase, letter-spacing 0.96px, cor Earth Dark `#30251c`

### Site Header (`.site-header`)
- Background: transparente (overlay sobre hero)
- Logo: `w-[38px]` (mobile) / `w-[240px]` (md+) / `w-[17vw]` (2xl)
- Menu button: ícone hambúrguer, cor Bone `#b9b2aa`
- Variantes: `.site-header--mobile`, `.site-header--top`

### Hero with CTA (`.hero-with-cta`)
- Background: Onyx `#1a1817`
- Full-viewport, imagem de fundo (video/foto)
- Grid layout com content-wrapper centralizado
- Heading H1 UPPERCASE + botão CTA abaixo
- Versões desktop/mobile com classes distintas

### Hover Card Section (`.hover-card-section`)
- Background: Onyx
- Contém cards com efeito flip (`.hover-card`, `.hover-card-front`, `.hover-card-back`)
- Container: `.hover-card-section__cards-wrapper` + `.hover-card-section__cards-container`
- Usado para: "Our Clubs", "Remedy Categories", "Private Experiences"

### Decorative Image Grid (`.decorative-image-grid`)
- Background: Onyx
- Grid assimétrico de imagens (`.decorative-image-grid__images`)
- Sem texto, apenas imagens decorativas

### Grid of Brands (`.grid-of-brands`)
- Logos de parceiros/mídia ("As Seen In")
- Background: Onyx

### Marquee / Scroll animado
- Scroll horizontal contínuo para logos ou textos

---

## 7. Layout & Espaçamento

### Breakpoints (Tailwind)

| Breakpoint | Prefixo | Uso observado |
|---|---|---|
| Mobile | (padrão) | Layout único, menu hambúrguer |
| Small | `sm:` | Grid 2 colunas, ajustes de posição |
| Medium | `md:` | Layout expandido, flex-row, ocultar mobile |
| Large | `lg:` | Grid 3–4 cols, bordas laterais |
| XL | `xl:` | Grid 4 colunas, paddings fluidos |
| 2XL | `2xl:` | Tipografia fluida (vw units), padding maior |
| 3XL | `3xl:` | Margem extra-larga |

### Escala de Espaçamento (Tailwind 4px base)

| Classe | Valor |
|---|---|
| `gap-2` | 8px |
| `gap-3` | 12px |
| `gap-5` | 20px |
| `gap-6` | 24px |
| `gap-8` | 32px |
| `p-2` | 8px |
| `p-5` | 20px |
| `p-10` | 40px |
| `px-6` | 24px |
| `px-8` | 32px |
| `px-10` | 40px |
| `py-4` | 16px |
| `py-5` | 20px |
| `py-8` | 32px |
| `py-10` | 40px |
| `pt-20` | 80px |
| `mt-10` | 40px |
| `mt-12` | 48px |
| `my-14` | 56px |

### Container / Page Gutter
- `.page-gutter`: `px-10` (40px) padrão, `md:px-6` (24px), `2xl:px-[4.5vw]`
- Max-width de conteúdo: `max-w-[1200px]`, `max-w-6xl`, `max-w-[720px]`, `max-w-md`

---

## 8. Border & Radius

- **Border-radius:** `0px` em quase tudo (estilo flat/editorial). Exceções: `10px` e `12px` em elementos de terceiros (reviews widget)
- **Bordas:** `1px solid` nas cores Earth Light (`#4b443c`) e Bone Light (`#cdc9c2`)
- **Padrão de bordas em listas/botões:** `border-t border-x last:border-b` (bordas compostas tipo tabela)

---

## 9. Sombras

Nenhuma box-shadow ou text-shadow encontrada — visual completamente flat, profundidade criada por contraste de cor e opacidade.

---

## 10. Animações & Transições

| Classe | Valor | Uso |
|---|---|---|
| `transition` | padrão (150ms) | Hover geral |
| `transition-colors` | cores | Mudança de cor |
| `transition-opacity` | opacidade | Fade in/out |
| `duration-150` | 150ms | Micro-interações |
| `duration-500` | 500ms | Transições médias |
| `duration-700` | 700ms | Transições longas |
| `duration-[2s]` | 2000ms | Animações de entrada |
| `duration-[3s]` | 3000ms | Animações lentas (hero) |
| `ease-in-out` | padrão | Easing geral |
| `ease-out` | suave saída | Modais, dropdowns |
| `ease-out-expo` | expo | Animações hero suaves |
| `delay-500/700/1000` | delays | Animações sequenciais |

---

## 11. Z-Index Scale

| Classe | Valor | Uso |
|---|---|---|
| `z-0` | 0 | Base |
| `z-10` | 10 | Elementos elevados |
| `z-20` | 20 | Overlays leves |
| `z-30` | 30 | Site banner (fixed) |
| `z-40` | 40 | Dropdowns |
| `z-50` | 50 | Modais, menu mobile |

---

## 12. Estrutura de Páginas

A homepage segue este fluxo de seções:

1. **Site Banner** — Anúncio fixo no topo (promoção/novo produto)
2. **Site Header** — Logo + menu hambúrguer (transparente, sobre o hero)
3. **Hero with CTA** — Full-screen, imagem/vídeo + headline H1 + botão "Reservations"
4. **Hover Card Section** — "Our Clubs" (cards interativos com flip)
5. **Decorative Image Grid** — Grid fotográfico sem texto
6. **Hover Card Section** — "Remedy Categories"
7. **Hero with CTA** — "Our Remedies" (secundário)
8. **Hover Card Section** — "Private Experiences"
9. **Grid Stack** — "Experience Self-Care Made Social" (CTA de membership)
10. **Grid of Brands** — "As Seen In" (logos de mídia)
11. **Footer** — Links + formulário Klaviyo de email

---

## Resumo do Design System

O design system da Remedy Place é **dark, flat e editorial** — usa uma paleta monocromática terrosa quente, tipografia com dois pesos de uma só família customizada (Beausite), zero border-radius em componentes próprios, e espaçamento generoso. A linguagem visual remete a clubes de bem-estar de alto padrão, com movimentos lentos e suaves e profundidade criada exclusivamente por contraste de cor.