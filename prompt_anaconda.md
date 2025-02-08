Os ambientes criados no conda fora do C:\Users\andre.rocha\AppData\Local\anaconda3\envs\

são acessíveis apenas pela referência do local onde foi criado, nesse caso, pelo interpretador do VSCode
na pasta do projeto: conda activate "C:\Users\andre.rocha\OneDrive - SLC Participacoes S.A\Demandas\@2025-Demandas\Github_Projects\langchain-february\.conda"

Name-based reference of Conda environments only works for environments located in one of the directories listed in the envs_dirs configuration option (see conda config --describe envs_dirs). By default this corresponds to the envs/ subdirectory in the Conda installation. If you create an env outside of one of these directories, then you cannot use a name to reference it. Instead, one must activate it by its path:


Option 1: Clone Into Directory
One option to use conda activate B3, is to recreate your B3 env in the default directory. You can use the --clone flag to accomplish this.
conda create --clone path/to/the/nameless_env -n named_env

Option 2: Add Parent Directory
Alternatively, you can add the parent directory of the environment in question to the envs_dirs configuration option.
conda config --append envs_dirs /path/to/the/parent_dir

Option 3: Symbolic Link
Another possibility is to create a symbolic link in one to the envs_dirs folders to the environment folder. It seems to work, but it is not a common practice, so it may have downsides that are unreported.


--------

## Variáveis de ambiente com .env
Utilizando a biblioteca python-dotenv. Utilizando essa biblioteca utilizo para buscar os valores e levar para dentro do código.

### Exemplo
USUARIO = andre
EMAIL = ${USUARIO}@hotmail.com

--------

