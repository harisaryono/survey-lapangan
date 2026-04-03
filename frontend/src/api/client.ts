const API_BASE = "http://127.0.0.1:8000/api/v1";

export type LoginPayload = {
  username: string;
  password: string;
};

export async function login(payload: LoginPayload) {
  const response = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("Login gagal");
  }

  return response.json();
}

export async function fetchSurveys(token?: string) {
  const response = await fetch(`${API_BASE}/surveys`, {
    headers: token ? { Authorization: `Bearer ${token}` } : {},
  });

  if (!response.ok) {
    throw new Error("Gagal memuat survei");
  }

  return response.json();
}

export async function createSurvey(data: Record<string, unknown>, token?: string) {
  const response = await fetch(`${API_BASE}/surveys`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Gagal membuat survei");
  }

  return response.json();
}
