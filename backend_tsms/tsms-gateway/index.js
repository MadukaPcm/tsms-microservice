const { ApolloServer, gql } = require('apollo-server');
const { ApolloGateway } = require('@apollo/gateway');
const { readFileSync } = require('fs');

const supergraphSdl = readFileSync('./supergraph.graphql').toString();

// Initialize an ApolloGateway instance and pass it
// the supergraph schema as a string
const gateway = new ApolloGateway({
    supergraphSdl,
});

// Pass the ApolloGateway to the ApolloServer constructor
const server = new ApolloServer({
    gateway,
});

server.listen().then(({ url }) => { 
    console.log(`Gateway ready at ${url}`);
}).catch(err => { console.error(err) });

// server.listen().then(({ url }) => {
//   console.log(`🚀 Server ready at ${url}`);
// });Supporting links forbuilding api gateway:::::::;https://www.apollographql.com/docs/rover/commands/supergraphs,https://www.apollographql.com/docs/federation/gateway/,sudo rover supergraph compose --config ./supergraph-config.yaml > supergraph.graphql
// ┌─
// [jackroot7 @jackroot7]─[~/Videos/DTP / Backend Services / dtp_api_gateway]└──╼ $sudo rover supergraph compose--config. / supergraph - config.yaml > supergraph.graphql
// composing supergraph with Federation v2 .0 .5.┌─[jackroot7 @jackroot7]─[~/Videos/DTP / Backend Services / dtp_api_gateway]└──╼ $node index.js
// Gateway ready at http: //localhost:4000/