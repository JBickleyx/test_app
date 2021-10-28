from logging import debug
from flask_app import app
from flask_app.controllers import owners, animals


if __name__ == '__main__':
  app.run(debug=True);


# GET render
# POST redirect

# /owners/new -> GET
# /owners/create -> POST
# /owners/owner_id/edit -> GET
# /owners/owner_id/update -> POST
# /owners/owner_id/delete -> GET
# /owners/owner_id/destrow -> POST

# GET VS POST
# new vs create
# edit vs update
# delete vs destroy

## /animals/new -> GET
# /animals/create -> POST
# /animals/animal_id/edit -> GET
# /animals/animal_id/update -> POST
# /animals/animal_id/delete -> GET
# /animals/animal_id/destrow -> POST