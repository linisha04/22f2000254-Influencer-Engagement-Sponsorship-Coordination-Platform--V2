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
        signout(state){
            state.user=null;
            state.token=null;
        }
       
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
            commit('signout');
        }
       

    }
});