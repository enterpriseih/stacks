const state = {
  user: {},
}
const getters = {
  user: (state) => {
    return state.user
  },
}

const actions = {
  saveUser({
    commit
  }, data) {
    commit('SAVEUSER', data)
  },
}
const mutations = {
  ['SAVEUSER'](state, payload) {
    state.user = payload
  }
}
export default {
  state, getters, actions, mutations
}
