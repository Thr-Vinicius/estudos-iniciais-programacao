const express = require('express');
const app = express();

app.use(express.static('public'));

app.get('/api/pokemon/:nome', async (req, res) => {
  try {
    const url = `https://pokeapi.co/api/v2/pokemon/${req.params.nome.toLowerCase()}`;
    const resp = await fetch(url);

    if (!resp.ok) {
      throw new Error('Não encontrado');
    }

    const dados = await resp.json();

    res.json({
      nome: dados.name,
      foto: dados.sprites.front_default
    });
  } catch (erro) {
    res.status(404).json({ erro: 'Não encontrado' });
  }
});

app.listen(3000, () => {
  console.log('Servidor rodando em http://localhost:3000');
});