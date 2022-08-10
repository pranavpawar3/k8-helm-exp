Steps to build the app image; (It's already built and pushed to my docker hub account, please pull it from there)

```bash
docker build -f Dockerfile -t vanilla-image .
docker tag vanilla-image pranavpawar3/vanilla-image
docker push pranavpawar3/vanilla-image
```