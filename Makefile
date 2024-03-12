build:
	docker build -t  ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_IMAGE}/${GAR_IMAGE}:prod .

push:
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_IMAGE}/${GAR_IMAGE}:prod

deploy:
	gcloud run deploy --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_IMAGE}/${GAR_IMAGE}:prod --memory ${GAR_MEMORY} --region ${GCP_REGION} --env-vars-file .env.yaml
