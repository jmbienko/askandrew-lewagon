build:
	docker build -t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_IMAGE}/${GAR_IMAGE}:post .

push:
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_IMAGE}/${GAR_IMAGE}:post

deploy:
	gcloud run deploy --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_IMAGE}/${GAR_IMAGE}:post \
	--memory ${GAR_MEMORY} --region ${GCP_REGION} --env-vars-file .env.yaml \
	--min-instances 1 --no-cpu-throttling

uvi:
	 uvicorn askandrew.api.api:app --reload
