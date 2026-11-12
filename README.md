# Combate T20

Painel de combate para **Tormenta20 (Jogo do Ano)**: PV/PM com temporários, poderes, ataques e dano explicados, calculadora e descanso. Funciona offline e salva os dados no próprio aparelho.

## Usar

- **No navegador:** https://psalmazzi.github.io/MobileT20/
  No celular, use *Adicionar à tela inicial*: vira um ícone que abre em tela cheia e funciona sem internet.
- **APK (Android):** baixe o `CombateT20.apk` em **Releases → apk** e instale (permita *fontes desconhecidas*).

Os personagens ficam salvos só no aparelho/navegador de cada pessoa. Para levar de um lugar a outro: Início → ⚙ → **Copiar JSON** e **Colar JSON**.

## Como o repositório funciona

| Pasta | O quê |
|---|---|
| `web/` | O app (um único `index.html`), manifesto PWA, service worker e ícones. É o que vai para o site. |
| `android/` | Projeto Android mínimo: uma WebView que abre `assets/index.html` de dentro do APK. Sem internet, só a permissão de vibração. |
| `.github/workflows/pages.yml` | Publica `web/` no GitHub Pages a cada mudança. |
| `.github/workflows/android.yml` | Compila o APK a cada mudança e atualiza o release `apk`. |
| `tools/preparar_web.py` | Copia um `index.html` novo para `web/` e injeta o manifesto e o service worker. |

### Assinatura do APK

O APK é assinado com a chave em `android/keystore/combate-t20.jks` (senha `combate-t20`). Ela é **pública** (está no repositório) para que todas as versões tenham a mesma assinatura e possam ser atualizadas por cima sem perder os dados. Serve para uso pessoal e entre amigos; não use essa chave para publicar na Google Play.

Para usar uma chave privada, crie em *Settings → Secrets and variables → Actions*: `KEYSTORE_BASE64` (o `.jks` em base64), `KEYSTORE_PASSWORD`, `KEY_ALIAS`, `KEY_PASSWORD`. Atenção: trocar de chave exige desinstalar a versão anterior (o que apaga os dados do app — faça backup antes com *Copiar JSON*).

### Compilar localmente (Android Studio)

Abra a pasta `android/` no Android Studio e use *Build → Build APK(s)*. O `assets/index.html` já vem atualizado no repositório.
