require("@nomiclabs/hardhat-waffle");

task("accounts", "Prints the  list of accounts", async(taskArgs, hre) => {
  const accounts = await hre.ethers.getSigners();
  for (const account of accounts) {
    console.log(account.address);
  }
});

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.17",
  networks: {
    goerli: {
      url: 'https://eth-goerli.g.alchemy.com/v2/FEuEqnOxyWSNOk4YLqdQC5w7xI70u8Ru',
      accounts: ['6ed2681cb1d3feddf6260d514cc8eb87fa70e3433702440604a6012e85ee9a18']
    }
  }
};
