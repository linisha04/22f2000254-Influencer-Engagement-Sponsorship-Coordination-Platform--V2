import { createStore } from "vuex";

export default createStore({
    state(){
        return {
            user: {
                token: null,
                roles: [],
            
            

            },
        
        }
    },
    mutations: {
        setUser(state, value){
            localStorage.setItem("user", JSON.stringify(value));
            state.user = value ;
            // || { token: null, roles: [] }
        },
        clearUser(state) {
            state.user = { token: null, roles: [] };
            localStorage.removeItem('user');
          },
       
    },
    getters: {
        getRoles(state){
            return state.user["roles"];
        },
        getToken(state){
            return state.user["token"] ;
        },

       
     
    },
    actions:{
        logout({ commit }){
            commit('clearUser');
        }
       

    }
});