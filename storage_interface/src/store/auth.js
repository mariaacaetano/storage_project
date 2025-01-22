import { defineStore } from 'pinia';
import api, { setAuthToken } from '../api/api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
  }),

  actions: {
    async login(email, password) {
      try {
        const response = await api.post('customuser/login/', { email, password });
        this.token = response.data.token;
        localStorage.setItem('token', this.token);
        setAuthToken(this.token);
      } catch (error) {
        console.error('Login error:', error);
        throw error;
      }
    },

    async fetchUser() {
      if (!this.token) return;

      try {
        const response = await api.get('customuser/employees/');
        this.user = response.data;
      } catch (error) {
        console.error('Fetch user error:', error);
      }
    },

    logout() {
      this.user = null;
      this.token = null;
      localStorage.removeItem('token');
      setAuthToken(null);
    },
  },
});
