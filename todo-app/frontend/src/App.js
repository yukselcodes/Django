import React from 'react';


class App extends  React.Component {

    formatName = (user) => {
        return user.firstname + " " + user.lastname
    }

    getTime = () => {
        return new Date().toLocaleTimeString()
    }

    getElement = () => {
        const user  = {
            'firstname': 'Yuksel',
            'lastname': 'Ozdemir'
        }
        return (
            <div>
                <h1> Hello {this.formatName(user)}</h1>
                <h3> Time is {this.getTime()}</h3>
            </div>
        )

    }
    render() {
        return this.getElement()
    }
}
export default App;
