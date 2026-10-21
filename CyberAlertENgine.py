print("="*50)
print("Seja bem-vindo ao Cyber Alert Engine")
print("="*50)


hostname = input("Hostname: ")
porta = int(input("Porta: "))
cvss = float(input("CVSS: "))
firewall = input("Firewall ativo (s/n): ").lower()

if cvss >= 8 and firewall == "n":
    risco = "CRÍTICO"
    acao = "Ativar firewall e corrigir a falha"

elif cvss >= 8:
    risco = "ALTO"
    acao = "Corrigir a vulnerabilidade"

elif cvss >= 4 and (porta == 22 or porta == 3389):
    risco = "ALTO"
    acao = "Restringir acesso à porta"

elif cvss >= 4:
    risco = "MÉDIO"
    acao = "Planejar uma correção"

else:
    risco = "BAIXO"
    acao = "Continuar monitorando"

print("\n=== RESULTADO ===")
print("Host:", hostname)
print("Porta:", porta)
print("CVSS:", cvss)
print("Risco:", risco)
print("Ação recomendada:", acao)
