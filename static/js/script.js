import { 
    Address, 
    ProviderRpcClient, 
    TvmException 
  } from 'everscale-inpage-provider';
  
  const ever = new ProviderRpcClient();
  
  async function myApp() {
    if (!(await ever.hasProvider())) {
      throw new Error('Extension is not installed');
    }
  
    const { accountInteraction } = await ever.requestPermissions({
      permissions: ['basic', 'accountInteraction'],
    });
    if (accountInteraction == null) {
      throw new Error('Insufficient permissions');
    }
  
    const selectedAddress = accountInteraction.address;
    const dePoolAddress = new Address('0:bbcbf7eb4b6f1203ba2d4ff5375de30a5408a8130bf79f870efbcfd49ec164e9');