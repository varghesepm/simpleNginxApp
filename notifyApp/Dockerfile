FROM python:alpine3.14

ENV WORK_DIR="/usr/local/src/app"
ENV LOG_FILE="${WORK_DIR}/app.log"
# cron runs at every 20 mints
ENV CRON_SPEC="*/20 * * * *"

WORKDIR ${WORK_DIR}

COPY main.py requirements.txt ${WORK_DIR}/

RUN pip install -r requirements.txt
RUN echo "${CRON_SPEC} python ${WORK_DIR}/main.py >> ${LOG_FILE} 2>&1" > ${WORK_DIR}/crontab
RUN touch ${LOG_FILE}
RUN crontab ${WORK_DIR}/crontab
RUN crontab -l
CMD crond  && tail -f ${LOG_FILE}