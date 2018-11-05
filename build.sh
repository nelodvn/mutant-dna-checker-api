VERSION=v1.0.0

docker build . -f ./services/mutants/Dockerfile -t mutants
docker build . -f services/nginx/Dockerfile -t nginx
docker build . -f services/swagger/Dockerfile -t swagger

docker tag mutants nelodvn/mutants:$VERSION
docker tag nginx nelodvn/nginx:$VERSION
docker tag swagger nelodvn/swagger:$VERSION

docker push nelodvn/mutants:$VERSION
docker push nelodvn/nginx:$VERSION
docker push nelodvn/swagger:$VERSION
