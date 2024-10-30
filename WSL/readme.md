### **Passo a passo: Configurando VS Code com WSL e acessando a pasta "projetos"**

---

### **1. Baixar e instalar a extensão WSL no VS Code**
1. Abra o **Visual Studio Code** no Windows.
2. Vá para a aba de **Extensões** (ou use `Ctrl+Shift+X`).
3. Na barra de pesquisa, digite:  
   ```
   Remote - WSL
   ```
4. Clique em **"Install"** para instalar a extensão **Remote - WSL**.
5. Após a instalação, reinicie o VS Code, se necessário.

---

### **2. Criar uma pasta chamada "projetos" na `home` usando o WSL**

1. Abra o **WSL** (pesquise "WSL" ou "Ubuntu" no menu Iniciar).
2. No terminal, digite:
   ```bash
   cd ~
   mkdir projetos
   cd projetos
   ```
3. Verifique se a pasta foi criada com:
   ```bash
   ls
   ```
   - O comando deve mostrar a pasta "projetos".

---

### **3. Acessar a pasta usando o Git Bash**

1. Abra o **Git Bash** no Windows.
2. Navegue até a pasta "projetos" com:
   ```bash
   cd //wsl$/Ubuntu/home/projetos/
   ```
3. Digite:
   ```bash
   ls
   ```
   - Se tudo estiver correto, você verá a pasta "projetos".

---

### **4. Acessar a pasta "projetos" pelo Explorador de Arquivos do Windows**

1. Abra o **Explorador de Arquivos**.
2. Na barra de endereços, digite:
   ```
   \\wsl$\Ubuntu\home\projetos\
   ```
3. Pressione **Enter**.  
   Agora você pode ver e gerenciar os arquivos dentro dessa pasta diretamente pelo Windows.

---

### **Dica Extra: Abrir a pasta diretamente no VS Code**

1. No terminal do **WSL**, navegue até a pasta:
   ```bash
   cd ~/projetos
   ```
2. Abra a pasta no VS Code com:
   ```bash
   code .
   ```
   - Isso abrirá o VS Code diretamente com a pasta "projetos" como seu workspace.

---

Agora você tem a pasta configurada, pode navegar por ela tanto no WSL quanto no Git Bash e Explorador de Arquivos, e integrá-la facilmente com o VS Code!