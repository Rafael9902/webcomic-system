export function getUserSession(): string | null {
  return sessionStorage.getItem("token");
}

export function saveSessionToken(token: string): void{
  sessionStorage.setItem("token", token);
}
