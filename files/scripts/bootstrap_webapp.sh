curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | tac | tac | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm install --lts
